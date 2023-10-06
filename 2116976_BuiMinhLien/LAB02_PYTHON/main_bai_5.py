from datetime import datetime
from sinh_vien import SinhVien
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSv

#sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", datetime.strptime("23/6/1999", "%d/%m/%Y"), 80)
#sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiCQ(1957692, "Thái Thị Thu", datetime.strptime("15/8/1998", "%d/%m/%Y"), "Cao đẳng", 2) 
sv4 = SinhVienPhiCQ(2899324, "Trần Thanh Tâm", datetime.strptime ( "27/8/2009", "%d/%m/%Y"), "Cao đẳng", 2)
sv5 = SinhVienPhiCQ(2994544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2000", "%d/%m/%Y"), "Trung cấp", 2.5)
# sv6 = SinhVienChinhQuy(2984567, "Nguyễn Thành Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiCQ(2984545, "Nguyễn Thanh Thanh", datetime.strptime("29/10/1999", "%d/%m/%Y"), "Trung cấp", 2.5) 
# sv8 = SinhVienChinhQuy(2904679, "Võ Hoài Nam", datetime.strptime("4/1/2009", "%d/%m/%Y"), 78)

dssv = DanhSachSv()
# dssv.themSV(sv1)
# dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
# dssv.themSV(sv6)
dssv.themSV(sv7)
# dssv.themSV(sv8)

dssv.xuat()

vt = dssv.timSVTheoMs(2000324)
print(f"Sinh viên ở vị trí thứ {vt + 1} trong danh sách")

kq = dssv.timSvTheoLoai("chinhquy") 
print("Danh sách sinh viên theo loại:") 
for sv in kq: 
    print(sv)