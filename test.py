from encoder.CRC_8 import *
def test_crc (data, generator):
    crc_code = crc_compute(data, generator)
    transmitted_data = data + crc_code
    print(f"remainder: {crc_code}")
    print(f"transmitted data: {transmitted_data}")
    if crc_check(transmitted_data, generator):
        print("No error detected")



test_crc("1011001", "1101")