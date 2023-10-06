class DSPS:
    def __init__(self) -> None:
        self.ds = []

    def ThemPhanSo(self, phanSo):
        self.ds.append(phanSo)

    def laPhanSoAm(self):
        return (self.tu * self.mau) < 0
    
    def DemPhanSoAm():
        dem = 0
        for item in DSPS:
            if DSPS.laPhanSoAm(item):
                dem += 1
        return dem
    def __str__(self) -> str:
        return str(self.ds)