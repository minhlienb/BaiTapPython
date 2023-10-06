from sinh_vien import SinhVien 
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int) -> None: 
        super().__init__(maSo, hoTen, ngaySinh)
        self.thoiGianDaoTao = tgdt
        self.trinhDo = trinhdo
    def ___str_(self) -> str:
        return super().___str__() + "\t{self.trinhDo}\t{self.thoiGianDaoTao}"
    