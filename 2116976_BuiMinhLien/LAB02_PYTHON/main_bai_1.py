from datetime import datetime

from sinhVien import SinhVien, DanhSachSV
import csv

sv1 = SinhVien(2116976, "Bùi Minh Liên",
               datetime.strptime("19/09/2003", "%d/%m/%Y"))
sv2 = SinhVien(2115230, "Lê Trần gia My",
               datetime.strptime("18/09/2003", "%d/%m/%Y"))
sv3 = SinhVien(2115892, "Trần Lê Anh Dũng",
               datetime.strptime("15/09/1999", "%d/%m/%Y"))
sv4 = SinhVien(2114569, "Lê Đại Hải Nam",
               datetime.strptime("13/02/2002", "%d/%m/%Y"))
sv5 = SinhVien(2111111, "Hoàng Trần Phương Nam",
               datetime.strptime("26/09/2003", "%d/%m/%Y"))
sv6 = SinhVien(2119632, "Nguyễn Hoàng Thanh Tú",
               datetime.strptime("19/08/2002", "%d/%m/%Y"))
# sv.xuat()
ds = DanhSachSV()
ds.themSinhVien(sv1)
ds.themSinhVien(sv2)
ds.themSinhVien(sv3)
ds.themSinhVien(sv4)
ds.themSinhVien(sv5)
ds.themSinhVien(sv6)
ds.xuat()

print(ds.timSvTheoMssv(2116976))


########## Đọc data từ file
""" file = open("danhsachSV.txt", "r", encoding="utf8")
read = file.readlines()
listSv = []
sv = []
for i in read:
    if i not in listSv:
        listSv.append(i.strip())
print("\nDanh Sách Sinh Viên:\n",listSv) """

#print(str(DanhSachSV.xoaSvTheoMssv(2116976)))
print(str(ds.timVTSvTheoMssv(2119632)))