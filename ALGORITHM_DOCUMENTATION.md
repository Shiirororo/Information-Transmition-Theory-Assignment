# ERROR DETECTION CODES SIMULATION PROJECT

This document describes the implemented error detection algorithms, project layout, example usage, and testing instructions.

---

## Project structure

- `encoder/` — Error detection algorithms package
   - `__init__.py` — Package exports
   - `parity.py` — Parity check (even/odd)
   - `CRC.py` — Cyclic Redundancy Check

- `noise/` — Noise injection utilities
- `test/` — Testing utilities and simulator
- `tools/` — GUI tools (CRC visualizer)
- `main.py` — Launcher (opens visualizer)
- `ASCII.csv` — ASCII reference table

---

## Algorithms implemented

1. Parity check
   - `even_parity()`, `odd_parity()`, `parity_encode()`, `parity_check()`
   - Use case: single-bit error detection
   - Overhead: 1 bit per block

2. CRC (Cyclic Redundancy Check)
   - `modulo2_division()`, `modulo2_division_steps()`, `crc_compute()`, `crc_encode()`, `crc_check()`
   - Use case: burst error detection (storage, network)

---

## Example usage (Python)

```python
from encoder import crc_encode, crc_check

data = "1011001"
encoded = crc_encode(data, "1101")  # returns data with CRC appended
is_valid = crc_check(encoded, "1101")
```

---

## Testing

Run all algorithm tests:

```bash
python test_algorithms.py
```

Run CRC-specific tests:

```bash
python test.py
```

---

## Next steps

- Add error correction codes (Hamming, Reed-Solomon)
- Integrate with noise simulator
- Add performance benchmarks
- Improve visualizations

---

## Vietnamese translation (Tiếng Việt)

# DỰ ÁN MÔ PHỎNG MÃ PHÁT HIỆN LỖI

Tài liệu này mô tả các thuật toán phát hiện lỗi đã triển khai, cấu trúc dự án, ví dụ sử dụng và hướng dẫn kiểm thử.

---

## Cấu trúc dự án

- `encoder/` — Gói chứa các thuật toán phát hiện lỗi
  - `__init__.py` — Xuất các hàm/khối trong gói
  - `parity.py` — Kiểm tra chẵn/lẻ (Parity)
  - `CRC.py` — Cyclic Redundancy Check

- `noise/` — Công cụ chèn nhiễu
- `test/` — Công cụ kiểm thử và mô phỏng
- `tools/` — Công cụ giao diện (CRC visualizer)
- `main.py` — Trình khởi chạy (mở visualizer)
- `ASCII.csv` — Bảng tham chiếu ASCII

---

## Các thuật toán đã triển khai

1. Parity (kiểm tra chẵn/lẻ)
   - `even_parity()`, `odd_parity()`, `parity_encode()`, `parity_check()`
   - Trường hợp sử dụng: phát hiện lỗi 1 bit
   - Chi phí: 1 bit cho mỗi khối dữ liệu

2. CRC (Cyclic Redundancy Check)
   - `modulo2_division()`, `modulo2_division_steps()`, `crc_compute()`, `crc_encode()`, `crc_check()`
   - Trường hợp sử dụng: phát hiện lỗi dạng burst (lưu trữ, mạng)

---

## Ví dụ sử dụng (Python)

```python
from encoder import crc_encode, crc_check

data = "1011001"
encoded = crc_encode(data, "1101")  # trả về dữ liệu kèm CRC
is_valid = crc_check(encoded, "1101")
```

---

## Kiểm thử

Chạy toàn bộ kiểm thử:

```bash
python test_algorithms.py
```

Chạy kiểm thử CRC:

```bash
python test.py
```

---

## Bước tiếp theo

- Thêm mã sửa lỗi (Hamming, Reed-Solomon)
- Tích hợp với bộ mô phỏng nhiễu
- Thêm đo hiệu năng
- Cải thiện phần trực quan hóa

