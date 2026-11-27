def chuyen_chu_hoa(cac_dong):
    return [dong.upper() for dong in cac_dong]


def main():
    print("Nhập các dòng (một dòng trống để kết thúc):")
    cac_dong = []
    while True:
        try:
            dong = input()
        except EOFError:
            break
        if dong == "":
            break
        cac_dong.append(dong)
    print("Kết quả:")
    print("\n".join(chuyen_chu_hoa(cac_dong)))


if __name__ == "__main__":
    main()
