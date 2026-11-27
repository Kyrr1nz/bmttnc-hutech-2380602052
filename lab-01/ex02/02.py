from math import isfinite


def tinh_dien_tich(ban_kinh):
    if not isfinite(ban_kinh) or ban_kinh < 0:
        raise ValueError("Bán kính phải là số hữu hạn không âm.")
    return 3.14 * ban_kinh * ban_kinh


def main():
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    print(f"Diện tích hình tròn là: {tinh_dien_tich(ban_kinh):g}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
