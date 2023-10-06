from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"
    def _init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None: 
        self._maSo = maSo # khai báo kiểu truy xuất là protected self._hoTen = hoTen
        self._ngaySinh = ngaySinh
        
    @property
    def hoTen(self): 
        return self._hoTen

    @hoTen.setter
    def hoTen(self, hoTen: str): 
        self._hoTen = hoTen

    @property
    def mssv(self): 
        return self._maSo
    
    @mssv.setter
    def mssv(self, ms: int):
        if self.ktMsHopLe (ms): 
            self._maso = ms

    @staticmethod
    def ktMsHopLe(mssv: int):
        return len(str (mssv)) == 7
    
    def _str_(self) -> str:
        return f"{self._maSo}\t{self._hoTen}\t{self._ngaySinh}"
    