from collections import Counter


def dem_so_lan_xuat_hien(danh_sach):
    return dict(Counter(danh_sach))


def main():
    cac_tu = input("Nhập các từ cách nhau bằng khoảng trắng: ").split()
    print("Số lần xuất hiện của các phần tử:", dem_so_lan_xuat_hien(cac_tu))


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        raise SystemExit("Chưa nhập danh sách từ.")
