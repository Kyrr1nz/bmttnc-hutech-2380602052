from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        sinh_vien = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_tb)
        self.danh_sach.append(sinh_vien)
        return sinh_vien

    def tim_theo_id(self, ma_sv):
        return next((sv for sv in self.danh_sach if sv.id == ma_sv), None)

    def cap_nhat(self, ma_sv, ten, gioi_tinh, chuyen_nganh, diem_tb):
        sinh_vien = self.tim_theo_id(ma_sv)
        if sinh_vien is None:
            return False
        sinh_vien.cap_nhat(ten, gioi_tinh, chuyen_nganh, diem_tb)
        return True

    def xoa(self, ma_sv):
        sinh_vien = self.tim_theo_id(ma_sv)
        if sinh_vien is None:
            return False
        self.danh_sach.remove(sinh_vien)
        return True

    def tim_theo_ten(self, tu_khoa):
        tu_khoa = tu_khoa.strip().casefold()
        if not tu_khoa:
            raise ValueError("Tên cần tìm không được trống.")
        return [sv for sv in self.danh_sach if tu_khoa in sv.ten.casefold()]

    def sap_xep_theo_diem(self):
        self.danh_sach.sort(key=lambda sv: sv.diem_tb)

    def sap_xep_theo_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda sv: sv.chuyen_nganh.casefold())

    def hien_thi(self, danh_sach=None):
        if danh_sach is None:
            danh_sach = self.danh_sach
        if not danh_sach:
            print("Danh sách sinh viên trống.")
            return
        print(f"{'ID':<5} | {'Họ tên':<24} | {'Giới tính':<9} | "
              f"{'Chuyên ngành':<24} | {'Điểm TB':>7} | Học lực")
        for sv in danh_sach:
            print(f"{sv.id:<5} | {sv.ten:<24} | {sv.gioi_tinh:<9} | "
                  f"{sv.chuyen_nganh:<24} | {sv.diem_tb:>7.2f} | {sv.hoc_luc}")
