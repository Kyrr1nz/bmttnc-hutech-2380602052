def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]


def main():
    chuoi = input("Nhập chuỗi cần đảo ngược: ")
    print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(chuoi))


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        raise SystemExit("Chưa nhập chuỗi cần đảo ngược.")
