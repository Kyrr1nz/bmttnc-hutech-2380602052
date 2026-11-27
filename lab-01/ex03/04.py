from ast import literal_eval


def truy_cap_phan_tu(du_lieu):
    if not isinstance(du_lieu, tuple) or not du_lieu:
        raise ValueError("Cần nhập một Tuple không rỗng, ví dụ (1, 2, 3).")
    return du_lieu[0], du_lieu[-1]


def main():
    du_lieu = literal_eval(input("Nhập Tuple, ví dụ (1, 2, 3): "))
    dau, cuoi = truy_cap_phan_tu(du_lieu)
    print("Phần tử đầu tiên:", dau)
    print("Phần tử cuối cùng:", cuoi)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, SyntaxError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
