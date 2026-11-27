def chao_mung(ten, tuoi):
    if not ten.strip() or tuoi < 0:
        raise ValueError("Họ tên không được trống và tuổi phải không âm.")
    return f"Chào mừng, {ten.strip()}! Bạn {tuoi} tuổi."


def main():
    ten = input("Nhập họ tên của bạn: ")
    tuoi = int(input("Nhập tuổi của bạn: "))
    print(chao_mung(ten, tuoi))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
