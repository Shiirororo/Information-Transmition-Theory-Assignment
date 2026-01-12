import numpy as np
import matplotlib.pyplot as plt

def simulate_bch():
    n = 15
    k = 7
    t = 2
    
    snr_db = np.arange(0, 12, 1)
    ber_uncoded = []
    ber_bch = []

    num_bits = 150000

    for snr in snr_db:
        bits = np.random.randint(0, 2, num_bits)
        transmitted = 2 * bits - 1
        
        snr_linear = 10**(snr / 10.0)
        noise_std = np.sqrt(1 / (2 * snr_linear))
        noise = np.random.normal(0, noise_std, num_bits)
        received = transmitted + noise
        
        detected_bits = (received > 0).astype(int)
        
        errors_uncoded = np.sum(bits != detected_bits)
        ber_uncoded.append(errors_uncoded / num_bits)
        
        num_blocks = num_bits // n
        detected_bits_reshaped = detected_bits[:num_blocks*n].reshape((num_blocks, n))
        original_bits_reshaped = bits[:num_blocks*n].reshape((num_blocks, n))
        
        errors_after_bch = 0
        for i in range(num_blocks):
            block_errors = np.sum(detected_bits_reshaped[i] != original_bits_reshaped[i])
            if block_errors > t:
                errors_after_bch += block_errors
            
        ber_bch.append(errors_after_bch / (num_blocks * n))

    plt.figure(figsize=(10, 6))
    plt.semilogy(snr_db, ber_uncoded, 'o-', label='Uncoded')
    plt.semilogy(snr_db, ber_bch, 's-', label='BCH (15, 7, 2)')
    plt.grid(True, which='both')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.title('BCH Simulation Performance')
    plt.legend()
    plt.show()

simulate_bch()