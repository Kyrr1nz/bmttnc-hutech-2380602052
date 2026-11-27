def dao_nguoc_list(danh_sach):
    return danh_sach[::-1]


def main():
    chuoi = input("Nhập các số nguyên cách nhau bằng dấu phẩy (trống = []): ")
    cac_so = list(map(int, chuoi.split(","))) if chuoi.strip() else []
    print("Danh sách đảo ngược:", dao_nguoc_list(cac_so))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
