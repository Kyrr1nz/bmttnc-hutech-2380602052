import re


def tinh_tong_trong_chuoi(chuoi):
    cac_so = [int(so) for so in re.findall(r"[+-]?[0-9]+", chuoi)]
    tong_duong = sum(so for so in cac_so if so > 0)
    tong_am = sum(so for so in cac_so if so < 0)
    return tong_duong, tong_am


def main():
    chuoi = input("Nhập chuỗi chứa các số nguyên: ")
    tong_duong, tong_am = tinh_tong_trong_chuoi(chuoi)
    print("Giá trị dương:", tong_duong)
    print("Giá trị âm:", tong_am)


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        raise SystemExit("Chưa nhập chuỗi.")
