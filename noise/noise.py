import random 

def short_burst_error (bits: str, max_burst_length) -> str:
    bits = list(bits)
    start = random.randint(0, len(bits) - 1)
    burst_len = random.randint(1, max_burst_length)
    for i in range(start, min(len(bits), start + burst_len)):
        bits[i] = "1" if bits[i] == "0" else "0"

    return "".join(bits)

def single_error (bits: str) -> str:
    bits = list(bits)
    error_pos = random.randint(0, len(bits)-1)
    bits[error_pos] = "1" if bits[error_pos] == "0" else "0"
    return "".join(bits)

def multiple_error(bits: str, num_errors: int) -> str:
    bits = list(bits)
    n = len(bits)
    num_errors = min(num_errors, n)
    positions = random.sample(range(n), num_errors)
    for p in positions:
        bits[p] = "1" if bits[p] == "0" else "0"

    return "".join(bits)

def random_multiple_error(bits: str, min_err=2, max_err=8) -> str:
    k = random.randint(min_err, max_err)
    return multiple_error(bits, k)


# Generate function