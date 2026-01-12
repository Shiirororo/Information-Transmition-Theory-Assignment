import numpy as np

def hamming_encode(data_bits):
    """Mã hóa 4 bit dữ liệu thành 7 bit Hamming."""
    d = [int(b) for b in data_bits]
    # Khởi tạo mảng 7 bit (vị trí 0 không dùng để khớp với lý thuyết vị trí 1-7)
    # p1 p2 d1 p3 d2 d3 d4
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    
    encoded = [p1, p2, d[0], p3, d[1], d[2], d[3]]
    return encoded

def hamming_decode(received_bits):
    """Giải mã 7 bit, phát hiện và sửa lỗi 1 bit."""
    r = received_bits
    
    # Tính toán các bit Syndrome (S)
    s1 = r[0] ^ r[2] ^ r[4] ^ r[6]
    s2 = r[1] ^ r[2] ^ r[5] ^ r[6]
    s3 = r[3] ^ r[4] ^ r[5] ^ r[6]
    
    # Chuyển đổi nhị phân Syndrome (S3S2S1) sang số thập phân để tìm vị trí lỗi
    error_pos = s1 * 1 + s2 * 2 + s3 * 4
    
    if error_pos == 0:
        return r, "Không có lỗi."
    else:
        # Sửa lỗi bằng cách đảo bit tại vị trí error_pos (chú ý index mảng là pos-1)
        corrected_r = list(r)
        corrected_r[error_pos - 1] = 1 - corrected_r[error_pos - 1]
        return corrected_r, f"Phát hiện lỗi tại vị trí: {error_pos}. Đã sửa."

def extract_data(hamming_bits):
    """Trích xuất 4 bit dữ liệu gốc từ 7 bit Hamming."""
    # Vị trí dữ liệu là 3, 5, 6, 7 (index 2, 4, 5, 6)
    return [hamming_bits[2], hamming_bits[4], hamming_bits[5], hamming_bits[6]]

# --- CHƯƠNG TRÌNH CHÍNH ---
if __name__ == "__main__":
    # 1. Nhập dữ liệu
    input_data = "1101"
    print(f"1. Dữ liệu gốc: {input_data}")

    # 2. Mã hóa
    encoded = hamming_encode(input_data)
    print(f"2. Mã hóa Hamming (7,4): {encoded}")

    # 3. Giả lập lỗi khi truyền tin (đổi bit ở vị trí số 5)
    received = list(encoded)
    error_idx = 4 # Vị trí thứ 5
    received[error_idx] = 1 - received[error_idx] 
    print(f"3. Dữ liệu nhận được (bị nhiễu tại bit 5): {received}")

    # 4. Giải mã và sửa lỗi
    corrected, message = hamming_decode(received)
    print(f"4. Kết quả giải mã: {message}")
    print(f"   Dữ liệu sau khi sửa: {corrected}")

    # 5. Trích xuất dữ liệu gốc
    final_data = extract_data(corrected)
    print(f"5. Dữ liệu cuối cùng trích xuất được: {''.join(map(str, final_data))}")