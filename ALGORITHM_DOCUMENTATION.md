"""
ERROR DETECTION CODES SIMULATION PROJECT
==========================================

PROJECT STRUCTURE:
==================

encoder/                          # Error detection algorithms package
├── __init__.py                  # Package initialization with all exports
├── parity.py                    # Parity check (even/odd)
├── checksum.py                  # Checksum (1's & 2's complement)
├── VRC.py                       # Vertical Redundancy Check
└── CRC.py                       # Cyclic Redundancy Check

noise/                            # Noise simulation package
├── __init__.py
└── noise.py                      # Error injection functions

test/                             # Testing utilities
├── __init__.py
├── simulator.py                  # Simulation and test framework
└── __pycache__/

Main Files:
├── main.py                        # Main entry point
├── test.py                        # Test CRC implementation
├── data.py                        # Data processing utilities
├── test_algorithms.py             # Comprehensive algorithm tests
├── ASCII.csv                      # ASCII reference table
├── test_data.csv                  # Test results log
└── requirements.txt               # Project dependencies


ALGORITHMS IMPLEMENTED:
=======================

1. PARITY CHECK
   - even_parity()              Calculate even parity bit
   - odd_parity()               Calculate odd parity bit
   - parity_encode()            Encode data with parity bit
   - parity_check()             Verify parity
   
   Use Case: Single-bit error detection in communication
   Overhead: 1 bit per data block
   Capability: Detects single-bit errors, odd number of errors

2. CHECKSUM
   - ones_complement_checksum() Calculate 1's complement checksum
   - twos_complement_checksum() Calculate 2's complement checksum
   - checksum_encode()          Encode data with checksum
   - checksum_check()           Verify checksum
   
   Use Case: Multi-bit error detection (e.g., network protocols)
   Overhead: 8 bits (1 byte) per data block
   Capability: Detects most multi-bit errors, good for network data

3. VRC (VERTICAL REDUNDANCY CHECK)
   - vrc_encode()               Calculate VRC for single byte
   - vrc_check()                Verify VRC
   - vrc_multi_byte_encode()    Encode multiple bytes with VRC
   
   Use Case: 2D data error detection (multiple bytes)
   Overhead: 8 bits (1 byte) for multiple bytes
   Capability: Detects single-bit errors in each bit position

4. CRC (CYCLIC REDUNDANCY CHECK)
   - modulo2_division()         Perform XOR-based polynomial division
   - crc_compute()              Calculate CRC remainder
   - crc_encode()               Encode data with CRC
   - crc_check()                Verify CRC
   
   Use Case: Burst error detection (Ethernet, Wi-Fi, storage)
   Overhead: Depends on polynomial degree (typically 16-32 bits)
   Capability: Excellent error detection, detects burst errors


EXAMPLE USAGE:
==============

from encoder import parity_encode, parity_check

# Parity
data = "1101"
encoded = parity_encode(data, 'even')  # "11011"
is_valid = parity_check(encoded, 'even')  # True

# Checksum
from encoder import checksum_encode, checksum_check
data = "11010011"
encoded = checksum_encode(data, 'ones')
is_valid = checksum_check(encoded, 'ones', 8)  # True

# CRC
from encoder import crc_encode, crc_check
data = "1011001"
encoded = crc_encode(data, "1101")  # "1011001110"
is_valid = crc_check(encoded, "1101")  # True

# VRC
from encoder import vrc_encode, vrc_check
data = "01100001"
vrc = vrc_encode(data, 'even')
is_valid = vrc_check(data, vrc, 'even')  # True


ALGORITHM COMPARISON:
=====================

Algorithm  | Overhead | Error Detection | Use Case
-----------|----------|-----------------|----------
Parity     | 1 bit    | Single-bit      | Simple, low overhead
Checksum   | 8 bits   | Most multi-bit  | Networks, checksums
VRC        | 8 bits   | Single per col  | 2D data, matrix
CRC        | 3-32bit  | Burst errors    | Storage, wireless


ERROR TYPES DETECTED:
====================

1. Single Bit Error: ✓ Parity, VRC, CRC
2. Multiple Bit Error: ✓ Checksum, CRC (limited)
3. Burst Error: ✓ CRC (excellent), Checksum (limited)
4. Odd/Even number of errors: ✓ Parity (for odd)


TESTING:
========

Run comprehensive tests:
  python test_algorithms.py

Run CRC tests:
  python test.py

Run simulation with noise:
  python data.py


NEXT STEPS:
===========

1. Error correction codes (Hamming, Reed-Solomon)
2. Integration with noise simulation
3. Performance benchmarking
4. Real-world data testing
5. Visualization of error detection performance
"""
