from sinh_vien_chinh_quy import SinhVienChinhQuy 
from sv_phi_chinh_quy import SinhVienPhiCQ
from sinh_vien import SinhVien

class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien): 
        self.dssv.append(sv)

    def xuat (self):
        for sv in self.dssv: print(sv)

    def timSVTheoMs (self, ms: str):
        for i in range(len(self.dssv)): 
            if self.dssv[i].mssv == ms: 
                return i
            else:
                return -1
    def timSvTheoLoai(self, loai: str): 
        if loai == "chinh quy":
            return [sv for sv in self.dssv if isinstance (sv, SinhVienChinhQuy)] 
        return [sv for sv in self.dssv if isinstance (sv, SinhVienPhiCQ)]
# tìm sinh viên có điểm rèn luyện từ 80 trở lên
# tìm sinh viên có trình độ cao đẳng sinh trước 15/8/1999