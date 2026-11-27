from ast import literal_eval


def xoa_phan_tu(tu_dien, key):
    if key not in tu_dien:
        return False
    del tu_dien[key]
    return True


def main():
    tu_dien = literal_eval(input("Nhập Dictionary, ví dụ {'a': 1, 'b': 2}: "))
    if not isinstance(tu_dien, dict):
        raise ValueError("Dữ liệu phải là Dictionary.")
    chuoi_key = input("Nhập key (chuỗi: a hoặc 'a'; số: 1): ").strip()
    try:
        key = literal_eval(chuoi_key)
    except (ValueError, SyntaxError):
        key = chuoi_key
    if xoa_phan_tu(tu_dien, key):
        print("Đã xóa phần tử có key:", key)
    else:
        print("Không tìm thấy key:", key)
    print("Dictionary sau khi xử lý:", tu_dien)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, SyntaxError, TypeError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
