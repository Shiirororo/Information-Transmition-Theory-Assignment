import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

def simulate_ber():
    # SNR range from 0 to 11 dB
    snr_db = np.arange(0, 12, 1)  
    ber_hamming = []
    ber_repetition = []
    ber_uncoded = []
    
    # Increase num_bits for smoother curves at high SNR
    num_bits = 1000000 
    data = np.random.randint(0, 2, num_bits)

    for db in snr_db:
        snr_linear = 10**(db/10)
        # Noise standard deviation for BPSK
        sigma = np.sqrt(1 / (2 * snr_linear))
        
        # 1. Uncoded (BPSK Simulation)
        tx_uncoded = 2 * data - 1
        noise = sigma * np.random.randn(num_bits)
        rx_uncoded = tx_uncoded + noise
        decoded_uncoded = (rx_uncoded > 0).astype(int)
        ber_uncoded.append(np.mean(data != decoded_uncoded))

        # 2. Hamming (7,4) - Theoretical Approximation
        # Correction: Removed 'np.' from erfc
        p_bit = 0.5 * erfc(np.sqrt(snr_linear * (4/7)))
        # Probability of more than 1 error in 7 bits
        p_block_error = 1 - (1-p_bit)**7 - 7*p_bit*(1-p_bit)**6
        ber_hamming.append(p_block_error / 7)

        # 3. Repetition Code n=3 - Theoretical Approximation
        # Correction: Removed 'np.' from erfc
        p_bit_rep = 0.5 * erfc(np.sqrt(snr_linear * (1/3)))
        # Majority logic: Error if 2 or 3 bits are wrong
        p_error_rep = 3*(p_bit_rep**2)*(1-p_bit_rep) + p_bit_rep**3
        ber_repetition.append(p_error_rep)

    return snr_db, ber_uncoded, ber_hamming, ber_repetition

# Run simulation
snr, uncoded, hamming, repetition = simulate_ber()

# Plotting
plt.figure(figsize=(10, 7))
plt.semilogy(snr, uncoded, 'k--', linewidth=2, label='Uncoded (BPSK)')
plt.semilogy(snr, repetition, 'ro-', markersize=4, label='Repetition Code (n=3)')
plt.semilogy(snr, hamming, 'bs-', markersize=4, label='Hamming (7,4)')



plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('BER Performance Comparison: Hamming vs Repetition vs Uncoded')
plt.legend()
plt.ylim(1e-6, 1) # Set limit to see low error rates clearly
plt.show()