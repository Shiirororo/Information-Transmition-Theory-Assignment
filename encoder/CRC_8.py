def modulo2_division (data, poly):
    data = list (data)
    poly = list (poly)
    r = len(poly) - 1

    for i in range (len(data) - r):
        if data[i] == '1':
            for j in range (len(poly)):
                data[i + j] = str (int (data[i + j] != poly[j]))

    return ''.join (data[-r:])


def crc_compute (data: str, poly: str) -> str:
    r = len (poly) - 1
    data = data + '0' * r
    remainder = modulo2_division (data, poly)
    return remainder
def crc_check (received_data, poly):
    remainder = modulo2_division (received_data, poly)
    return all (bit == '0' for bit in remainder)