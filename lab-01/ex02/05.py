from decimal import Decimal, InvalidOperation


def tinh_luong(so_gio, luong_gio):
    so_gio, luong_gio = Decimal(str(so_gio)), Decimal(str(luong_gio))
    if not so_gio.is_finite() or not luong_gio.is_finite():
        raise ValueError("Số giờ và lương giờ phải hữu hạn.")
    if so_gio < 0 or luong_gio < 0:
        raise ValueError("Số giờ và lương giờ phải không âm.")
    gio_thuong = min(so_gio, Decimal(44))
    gio_them = max(Decimal(0), so_gio - Decimal(44))
    return (gio_thuong + gio_them * Decimal("1.5")) * luong_gio


def main():
    so_gio = input("Nhập số giờ làm việc trong tuần: ")
    luong_gio = input("Nhập mức lương theo giờ tiêu chuẩn: ")
    print(f"Số tiền thực lĩnh của nhân viên: {tinh_luong(so_gio, luong_gio):.2f}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, InvalidOperation, EOFError) as loi:
        raise SystemExit(f"Dữ liệu không hợp lệ: {loi}")
