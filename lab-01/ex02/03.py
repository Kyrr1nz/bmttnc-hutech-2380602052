def la_so_chan(so):
    return so % 2 == 0


def main():
    so = int(input("Nhập một số nguyên: "))
    print(f"{so} là số {'chẵn' if la_so_chan(so) else 'lẻ'}.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
