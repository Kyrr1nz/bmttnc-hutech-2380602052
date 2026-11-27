from QuanLySinhVien import QuanLySinhVien

MENU = """
CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN
1. Thêm sinh viên
2. Cập nhật thông tin sinh viên theo ID
3. Xóa sinh viên theo ID
4. Tìm kiếm sinh viên theo tên
5. Sắp xếp theo điểm trung bình (tăng dần)
6. Sắp xếp theo tên chuyên ngành (tăng dần)
7. Hiển thị danh sách sinh viên
0. Thoát
"""


def nhap_thong_tin():
    ten = input("Nhập họ tên: ")
    gioi_tinh = input("Nhập giới tính: ")
    chuyen_nganh = input("Nhập chuyên ngành: ")
    diem_tb = float(input("Nhập điểm trung bình (0-10): "))
    return ten, gioi_tinh, chuyen_nganh, diem_tb


def main():
    quan_ly = QuanLySinhVien()
    while True:
        print(MENU)
        try:
            lua_chon = input("Chọn chức năng: ").strip()
            if lua_chon == "0":
                print("Đã thoát chương trình.")
                break
            if lua_chon == "1":
                sv = quan_ly.them(*nhap_thong_tin())
                print(f"Đã thêm sinh viên có ID = {sv.id}.")
            elif lua_chon == "2":
                ma_sv = int(input("Nhập ID cần cập nhật: "))
                if quan_ly.tim_theo_id(ma_sv) is None:
                    print(f"Không tìm thấy sinh viên có ID = {ma_sv}.")
                else:
                    quan_ly.cap_nhat(ma_sv, *nhap_thong_tin())
                    print("Đã cập nhật thông tin sinh viên.")
            elif lua_chon == "3":
                ma_sv = int(input("Nhập ID cần xóa: "))
                if quan_ly.xoa(ma_sv):
                    print(f"Đã xóa sinh viên có ID = {ma_sv}.")
                else:
                    print(f"Không tìm thấy sinh viên có ID = {ma_sv}.")
            elif lua_chon == "4":
                ket_qua = quan_ly.tim_theo_ten(input("Nhập tên cần tìm: "))
                if ket_qua:
                    quan_ly.hien_thi(ket_qua)
                else:
                    print("Không tìm thấy sinh viên theo tên đã nhập.")
            elif lua_chon == "5":
                quan_ly.sap_xep_theo_diem()
                print("Đã sắp xếp theo điểm trung bình.")
                quan_ly.hien_thi()
            elif lua_chon == "6":
                quan_ly.sap_xep_theo_chuyen_nganh()
                print("Đã sắp xếp theo tên chuyên ngành.")
                quan_ly.hien_thi()
            elif lua_chon == "7":
                quan_ly.hien_thi()
            else:
                print("Lựa chọn không hợp lệ. Hãy chọn từ 0 đến 7.")
        except ValueError as loi:
            print(f"Dữ liệu không hợp lệ: {loi}")
        except (EOFError, KeyboardInterrupt):
            print("\nĐã thoát chương trình.")
            break


if __name__ == "__main__":
    main()
