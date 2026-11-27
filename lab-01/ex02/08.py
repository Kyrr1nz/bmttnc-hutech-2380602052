def loc_nhi_phan(chuoi):
    cac_so = [so.strip() for so in chuoi.split(",")]
    if any(len(so) != 4 or set(so) - {"0", "1"} for so in cac_so):
        raise ValueError("Mỗi số phải có đúng 4 chữ số 0 hoặc 1.")
    return [so for so in cac_so if int(so, 2) % 5 == 0]


def main():
    chuoi = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
    print(",".join(loc_nhi_phan(chuoi)))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
