chuỗi = "1;11;14"
sốlượng = "2;1;1"
MatHang = [
    "Áo Thun T-Shirt Nam",
    "Áo Khoác Bomber Nam",
    "Quần Jeans Nam",
    "Áo Sơ Mi Nữ",
    "Áo Polo Nam",
    "Áo Len Nữ",
    "Quần Kaki Nam",
    "Áo Hoodie Nữ",
    "Áo Thun Crop Top Nữ",
    "Áo Polo Nam",
    "Quần Jogger Nam",
    "Quần Legging Nữ",
    "Quần Khaki Nữ",
    "Quần Short Nam",
    "Quần Jean Nữ",
    "Váy Đầm Bodycon Nữ"
]

i = 0
for mamathang in chuỗi.split(';'):
    print(MatHang[int(mamathang)] + "Số Lượng: " + sốlượng.split(';')[i])
    i += 1