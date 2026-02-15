"""
CRC (Cyclic Redundancy Check) - Error Detection Algorithm
Detects multi-bit and burst errors using polynomial division
"""

def modulo2_division(data: str, poly: str) -> str:
    """
    Perform modulo-2 division (XOR-based division).
    
    Args:
        data: Binary string (data padded with zeros)
        poly: Generator polynomial as binary string
    
    Returns:
        Remainder after division
    """
    data = list(data)
    poly = list(poly)
    r = len(poly) - 1

    for i in range(len(data) - r):
        if data[i] == '1':
            for j in range(len(poly)):
                # XOR operation: 0 XOR 0 = 0, 1 XOR 1 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1
                data[i + j] = str(int(data[i + j] != poly[j]))

    return ''.join(data[-r:])


def modulo2_division_steps(data: str, poly: str):
    """Generator that yields intermediate states during modulo-2 division.

    Yields tuples (i, j, current_state) where:
      - i is the current window start index
      - j is the bit index within the polynomial just processed (0-based). If j is None,
        it indicates the window was skipped (leading bit 0) or a window boundary reached.
      - current_state is the current full working register as a string.

    At the end, yields ('remainder', remainder_str).
    """
    r = len(poly) - 1
    padded = data + '0' * r
    arr = list(padded)
    poly_list = list(poly)

    for i in range(len(arr) - r):
        if arr[i] == '1':
            # perform XOR bit-by-bit and yield after each bit
            for j in range(len(poly_list)):
                arr[i + j] = '1' if arr[i + j] != poly_list[j] else '0'
                yield (i, j, ''.join(arr))
            # window finished
            yield (i, None, ''.join(arr))
        else:
            # nothing to do for this window, yield state with j=None
            yield (i, None, ''.join(arr))

    remainder = ''.join(arr[-r:]) if r > 0 else ''
    yield ('remainder', remainder)


def crc_compute(data: str, poly: str) -> str:
    """
    Calculate CRC for given data and generator polynomial.
    
    Args:
        data: Binary string (original data)
        poly: Generator polynomial as binary string
    
    Returns:
        CRC remainder as binary string
    """
    r = len(poly) - 1
    # Pad data with zeros (number of zeros = degree of polynomial)
    padded_data = data + '0' * r
    remainder = modulo2_division(padded_data, poly)
    return remainder


def crc_encode(data: str, poly: str) -> str:
    """
    Encode data with CRC appended.
    
    Args:
        data: Binary string (original data)
        poly: Generator polynomial as binary string
    
    Returns:
        Data with CRC appended
    """
    crc = crc_compute(data, poly)
    return data + crc


def crc_check(received_data: str, poly: str) -> bool:
    """
    Check if received data has valid CRC.
    
    Args:
        received_data: Binary string (data + CRC)
        poly: Generator polynomial as binary string
    
    Returns:
        True if no error detected, False if error detected
    """
    remainder = modulo2_division(received_data, poly)
    # If remainder is all zeros, no error detected
    return all(bit == '0' for bit in remainder)
