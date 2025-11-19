import random
import pandas as pd
import csv
from encoder.CRC_8 import crc_compute
from noise.noise import *
ASCII = pd.read_csv('ASCII.csv', index_col=0)

def _n_bit_random(n):
    string = ""
    for _ in range(n):
        random.randint(0, 1)
        string += str(random.randint(0, 1))
    return string

def get_ASCII_binary_code(string: str) -> str:
    binary_code = ""
    for char in string:
        ascii_value = ASCII.loc[ASCII["Character"] == char, "Binary Value"].values[0]
        binary_code += ascii_value
    return binary_code
#8-bit to ASCII
def reverse_binary_to_ASCII(binary_code: str) -> str:
    message = ""
    for i in range(0, len(binary_code), 8):
        byte = binary_code[i:i+8]          # byte nhị phân, dạng "01000001"
        row = ASCII.loc[ASCII["Binary Value"] == byte, "Character"]
        if row.empty:
            raise ValueError(f"Byte {byte} không tìm thấy trong bảng ASCII!")
        message += row.values[0]
    return message

def test(generator: str):
    len_of_bits = random.randint(8, 32)
    data = _n_bit_random(len_of_bits)
    transmitted_data = data + crc_compute(data, generator)
    received_data = ""
    error = {
        0: "No Error",
        1: "Single Bit Error",
        2: "Multiple Bit Error",
        3: "Burst Error"
    }
    type_of_error = random.randint(0, 3)
    is_Error = False
    match type_of_error:
        case 0:
            received_data = transmitted_data
        case 1:
            received_data = single_error(transmitted_data)
            is_Error = True
        case 2:
            received_data = random_multiple_error(transmitted_data, min_err=2, max_err=2)
            is_Error = True
        case 3:
            received_data = short_burst_error(transmitted_data, max_burst_length=5)
            is_Error = True
            
    with open('test_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        item = [data, crc_compute(data, generator), transmitted_data, received_data,
                "Error" if is_Error else "No Error", error[type_of_error]]
        writer.writerow(item)

# print(reverse_binary_to_ASCII("0100100001100101011011000110110001101111"))  # Expect "Hello"