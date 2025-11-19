from test.simulator import get_ASCII_binary_code, reverse_binary_to_ASCII
from encoder.CRC_8 import *
def main():
    message = get_ASCII_binary_code("hello12345")
    


def test_simulator():
    message = get_ASCII_binary_code("Hello")
    print(message)
    print("Original message in binary:", reverse_binary_to_ASCII(message))


if __name__ == "__main__":
    test_simulator()