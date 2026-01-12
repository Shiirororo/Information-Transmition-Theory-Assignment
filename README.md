# CRC Error Detection Project Documentation

## Overview
This project implements error detection algorithms, focusing on Cyclic Redundancy Check (CRC), and provides a GUI visualizer for educational and demonstration purposes.

## Structure
- **main.py**: Entry point. Launches the CRC visualizer GUI.
- **encoder/**: Python package for error detection algorithms.
  - **CRC.py**: Implements CRC (Cyclic Redundancy Check) functions:
    - `modulo2_division`: Performs modulo-2 division (XOR-based) for CRC calculation.
    - `modulo2_division_steps`: Generator for step-by-step CRC division (used for visualization).
    - `crc_compute`: Computes CRC remainder for given data and polynomial.
    - `crc_encode`: Encodes data by appending CRC.
    - `crc_check`: Checks received data for CRC errors.
  - **__init__.py**: Imports CRC and (optionally) parity check functions for package use.
- **tools/**: Utility scripts.
  - **crc_visualizer.py**: Tkinter GUI to visualize CRC encoding, transmission, and error checking. Allows step-by-step animation of the CRC process.

## Usage
- Run `python main.py` to launch the CRC visualizer.
- In the GUI, enter binary data and a generator polynomial (binary, starting with '1').
- Visualize CRC encoding, transmission, and error detection interactively.

## CRC Algorithm
- **Encoding**: Data is padded with zeros (degree of polynomial), then modulo-2 division is performed. The remainder is appended to the data as CRC.
- **Checking**: Received data (data + CRC) is divided by the polynomial. If the remainder is all zeros, no error is detected.

## Visualization Features
- Step-by-step display of the division process.
- Animated highlighting of the current window and working register.
- Log of each step and result.
- Simulated transmission and reception stages.

## Extensibility
- The `encoder` package can be extended with other error detection codes (e.g., parity checks).
- The visualizer can be adapted for other algorithms.

## Requirements
- Python 3.x
- Tkinter (standard library)

## Authors
- Nguyễn Trọng Nhân
- Trần Bá Anh Hào
- Vũ Anh Quân
- Lê Nhật Trung


