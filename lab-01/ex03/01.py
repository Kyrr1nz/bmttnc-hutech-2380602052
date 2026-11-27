def tinh_tong_so_chan(danh_sach):
    return sum(so for so in danh_sach if so % 2 == 0)


def main():
    chuoi = input("Nhập các số nguyên cách nhau bằng dấu phẩy (trống = []): ")
    cac_so = list(map(int, chuoi.split(","))) if chuoi.strip() else []
    print("Tổng các số chẵn trong List là:", tinh_tong_so_chan(cac_so))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
