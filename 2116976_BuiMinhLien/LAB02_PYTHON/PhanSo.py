from danhSachPhanSo import DSPS

class PhanSo:
    def __init__(self, tu = 1, mau = 1) -> None:
        self.tu = tu
        self.mau = mau


    def rutGon(self):
        ps = PhanSo()
        ucln = self.TinhUCLN(self.tu, self.mau)
        ps.tu = self.tu // ucln
        ps.mau = self.mau // ucln
        return ps
        
    def __add__(self, other):
        rl = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        rl.tu = (self.tu * other.mau) + (other.tu * self.mau)
        rl.mau = self.mau * other.mau
        return rl

    def __sub__(self, other):
        rl = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        rl.tu = (self.tu * other.mau) - (other.tu * self.mau)
        rl.mau = self.mau * other.mau
        return rl.rutGon()
    
    def __mul__(self, other):
        rl = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        rl.tu = self.tu * other.tu
        rl.mau = self.mau * other.mau
        return rl.rutGon()
        
    def __truediv__(self, other):
        rl = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        rl.tu = self.tu * other.mau
        rl.mau = self.mau * other.tu
        return rl.rutGon()
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    @staticmethod
    def TinhUCLN(a,b):
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        return b

ps1 = PhanSo(3, 6)
ps2 = PhanSo(16, 4)
ps1.rutGon()
print(ps1)

print(ps1.__truediv__(ps2))

ds = DSPS()
ds.ThemPhanSo(ps1)

#math.isClose() tính sấp xỉ