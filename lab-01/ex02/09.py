from math import isqrt


def la_so_nguyen_to(so):
    if so < 2:
        return False
    return all(so % uoc != 0 for uoc in range(2, isqrt(so) + 1))


def main():
    so = int(input("Nhập một số nguyên: "))
    ket_qua = "là" if la_so_nguyen_to(so) else "không phải là"
    print(f"{so} {ket_qua} số nguyên tố.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
