def tao_tuple_tu_list(danh_sach):
    return tuple(danh_sach)


def main():
    chuoi = input("Nhập các số nguyên cách nhau bằng dấu phẩy (trống = []): ")
    cac_so = list(map(int, chuoi.split(","))) if chuoi.strip() else []
    print("List:", cac_so)
    print("Tuple từ List:", tao_tuple_tu_list(cac_so))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
