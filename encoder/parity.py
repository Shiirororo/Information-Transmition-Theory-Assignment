"""
Parity Check - Error Detection Algorithm
Detects single-bit errors by adding a parity bit
"""

def even_parity(data: str) -> str:
    """
    Calculate even parity bit for given data.
    Returns '1' if odd number of 1s, '0' if even number of 1s
    
    Args:
        data: Binary string
    
    Returns:
        Parity bit ('0' or '1')
    """
    ones_count = data.count('1')
    return '0' if ones_count % 2 == 0 else '1'


def odd_parity(data: str) -> str:
    """
    Calculate odd parity bit for given data.
    Returns '0' if odd number of 1s, '1' if even number of 1s
    
    Args:
        data: Binary string
    
    Returns:
        Parity bit ('0' or '1')
    """
    ones_count = data.count('1')
    return '1' if ones_count % 2 == 0 else '0'


def parity_encode(data: str, parity_type: str = 'even') -> str:
    """
    Encode data with parity bit appended at the end.
    
    Args:
        data: Binary string
        parity_type: 'even' or 'odd'
    
    Returns:
        Data with parity bit appended
    """
    if parity_type.lower() == 'even':
        parity_bit = even_parity(data)
    elif parity_type.lower() == 'odd':
        parity_bit = odd_parity(data)
    else:
        raise ValueError("parity_type must be 'even' or 'odd'")
    
    return data + parity_bit


def parity_check(received_data: str, parity_type: str = 'even') -> bool:
    """
    Check if received data has correct parity.
    
    Args:
        received_data: Binary string (data + parity bit)
        parity_type: 'even' or 'odd'
    
    Returns:
        True if no error detected, False if error detected
    """
    data = received_data[:-1]  # Remove parity bit
    parity_bit = received_data[-1]
    
    if parity_type.lower() == 'even':
        calculated_parity = even_parity(data)
    elif parity_type.lower() == 'odd':
        calculated_parity = odd_parity(data)
    else:
        raise ValueError("parity_type must be 'even' or 'odd'")
    
    return parity_bit == calculated_parity
