"""
Error Detection Codes Package
Contains implementations of various error detection algorithms:
- Parity Check (Even and Odd)
- CRC (Cyclic Redundancy Check)
"""

from .parity import (
    even_parity,
    odd_parity,
    parity_encode,
    parity_check
)

from .CRC import (
    modulo2_division,
    crc_compute,
    crc_encode,
    crc_check
)

__all__ = [
    # Parity
    'even_parity',
    'odd_parity',
    'parity_encode',
    'parity_check',
    # CRC
    'modulo2_division',
    'crc_compute',
    'crc_encode',
    'crc_check'
]
