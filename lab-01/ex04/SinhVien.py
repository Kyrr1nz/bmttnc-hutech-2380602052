from itertools import count
from math import isfinite


class SinhVien:
    _cac_id = count(1)

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.cap_nhat(ten, gioi_tinh, chuyen_nganh, diem_tb)
        self.id = next(self._cac_id)

    def cap_nhat(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        ten, gioi_tinh, chuyen_nganh = (
            ten.strip(), gioi_tinh.strip(), chuyen_nganh.strip()
        )
        diem_tb = float(diem_tb)
        if not all((ten, gioi_tinh, chuyen_nganh)):
            raise ValueError("Tên, giới tính và chuyên ngành không được trống.")
        if not isfinite(diem_tb) or not 0 <= diem_tb <= 10:
            raise ValueError("Điểm trung bình phải từ 0 đến 10.")
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb

    @property
    def hoc_luc(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        if self.diem_tb >= 6.5:
            return "Khá"
        if self.diem_tb >= 5:
            return "Trung bình"
        return "Yếu"
