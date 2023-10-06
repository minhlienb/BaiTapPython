import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *

mydb = mysql.connector.connect(
  host="localhost",
  user="lien",
  password="1234",
  #database="QLSinhVien"
  #database="QLBaiBao"
  database ="QLMonAn"
)

mycursor = mydb.cursor()

sqlInsertLop = "INSERT INTO Lop (ID, TenLop) VALUES (%s, %s)"
sqlInsertSinhVien = """INSERT INTO SinhVien (ID, HoTen, MaLop) VALUES (%s, %s, %s)"""
sqlDeletefromSinhVien = """DELETE FROM SinhVien"""

val = [
  ("1", "Mai Anh Đào", "2"),
  ("2", "Mai Thành Thân", "2"),
  ("3", "Phạm Thanh Thảo", "2"),
  ("4", "Trần Quốc Bảo Trung", "3"),
  ("5", "Thái Thành Lam", "3"),
  ("6", "Trần Văn Tám", "3"),
  ("7", "Nguyễn Công Thành", "4"),
  ("8", "Nguyễn Thị Lụa", "1"),
  ("9", "Phan Thanh Nga", "1"),
  ("10", "Trương Công Quyền", "4"),
  ("11", "Võ Thị Sáu", "1"),
  ("12", "Võ Tòng", "2"),
]


#=================================================================Các hàm dùng cho mysql
def ExecuteMultipleVal(strr:str, v):
  mycursor.executemany(strr, v)
  mydb.commit()
  print(mycursor.rowcount, "row was effected.")

def Execute(strr:str): # dùng để tạo ra bất kỳ thay đổi nào trên bảng
  mycursor.execute(strr)
  mydb.commit()
  print(mycursor.rowcount, "row was effected.")

def runSelect(strr:str): # dùng để hiển thị kết quả của dòng query
  mycursor.execute(strr)
  records = mycursor.fetchall()
  for row in records:
    print(row)
  print(mycursor.rowcount, "row was effected.")

def values_Of_Select(strr:str):
  result = []
  mycursor.execute(strr)
  records = mycursor.fetchall()
  for row in records:
    result.append(row)
  return result

def get_all_class():
  try:
    mycursor.execute("""select * from Lop""")
    records = mycursor.fetchall()

    for row in records:
      print("*"*50)
      print("Ma Lop", row[0])
      print("Ten Lop", row[1])

  except mysql.connector.Error as err:
    print("Đã có lỗi xảy ra: {}".format(err))


classes = ["CTK43", "CTK44A", "CTK44B", "CTK45A"]
def get_Info_students():
  try:
    mycursor.execute("""select * from SinhVien""")
    records = mycursor.fetchall()

    print("Danh sách sinh viên của các lớp là:")
    print("Mã số        Họ tên                  Mã lớp")
    print("_"*44)
    for row in records:
      print(f"{row[0]:<{9}}{row[1]:<{30}}{classes[int(row[2]) - 1]:<{10}}") # row[2]) -1 vì index mảng bắt đầu bằng 0

  except mysql.connector.Error as err:
    print("Đã có lỗi xảy ra: {}".format(err))


def getStudentbyQuery(selectQuery:str):
  try:
    print("Sinh viên được tìm thấy:")
    print("Mã số         Họ tên                    Mã lớp")
    print('========================================================')
    for row in values_Of_Select(f"{selectQuery}"):#hàm này có thể lưu nhiều giá trị nên phải dùng for
      print(f"{row[0]:<{9}}{row[1]:<{30}}{classes[int(row[2]) - 1]:<{10}}")
    
  except mysql.connector.Error as err:
    print("Đã có lỗi xảy ra: {}".format(err))


def get_student_by_id(val:str):
  try:
    print("Sinh viên được tìm thấy:")
    for row in values_Of_Select(f"Select * from SinhVien where id = {val}"):#hàm này có thể lưu nhiều giá trị nên phải dùng for
      print(f"{row[0]:<{9}}{row[1]:<{30}}{classes[int(row[2]) - 1]:<{10}}")
    
  except mysql.connector.Error as err:
    print("Đã có lỗi xảy ra: {}".format(err))



#---------------------------------------------------------------
# dùng cho bảng bài báo
sqlTaoBangBaiBao = """CREATE TABLE bai_bao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tieu_de VARCHAR(255) NOT NULL,
    noi_dung TEXT NOT NULL
);"""

sqlInsertBaiBao = """INSERT INTO BaiBao (TieuDe, NoiDung) VALUES (%s,%s)"""
feeds = [
  ("<h1>CEO Mai Triều Nguyên: Người dùng giờ thông minh hơn, họ không bỏ 10 đồng ra chỉ để dùng được có 2 đồng</h1>", "<p>Mai Triều Nguyên là một doanh nhân nổi tiếng, đồng thời cũng là Tổng Giám đốc của Công ty TNHH Mai Nguyên, một địa chỉ bán lẻ uy tín các sản phẩm công nghệ trong hàng chục năm nay của người tiêu dùng Việt. Ông đã góp phần quan trọng vào sự phát triển của thế giới công nghệ hiện đại. Với hơn 21 năm kinh nghiệm làm việc trong ngành, ông đã chứng kiến nhiều xu hướng và những thay đổi mà người tiêu dùng tiếp cận cũng sử dụng các sản phẩm công nghệ từ những ngày đầu tiên, cho tới thời điểm công nghệ đang dần trở thành một phần của đời sống con người.</p>"),
  ("<h1>Tại sao nhiều người cho rằng người ngoài hành tinh phải có hình người?</h1>","<h2>Hình dáng con người là sự lựa chọn tốt nhất cho sự sống thông minh.</h2> <p>Trước hết, chúng ta phải đưa ra một tiền đề rõ ràng, đó là cái mà chúng ta gọi là người ngoài hành tinh là chỉ những dạng sống có trí tuệ cao và văn minh chứ không phải một số vi sinh vật hay động vật, thực vật cấp thấp.Bởi nếu chỉ xét đến sự tồn tại của sự sống thì hình thức của sự sống ngoài hành tinh có thể rất đa dạng, thậm chí ngoài sức tưởng tượng của chúng ta.</p> <p>Nhưng nếu muốn xét đến sự phát triển của trí tuệ và văn minh thì hình thức sống không thể quá tùy tiện mà cần phải đáp ứng một số điều kiện cơ bản.Ví dụ, sự sống thông minh đòi hỏi khả năng não bộ tương đối lớn để lưu trữ và xử lý lượng lớn thông tin. Cuộc sống thông minh cũng cần một mức độ linh hoạt và phối hợp nhất định để thích ứng với nhiều môi trường và thách thức phức tạp khác nhau.</p>"),
  ("<h1>Tiêu đề 3</h1>","<p>Nội dung 3</p>"),
  ("<h1>Tiêu đề 4</h1>","<p>Nội dung 4</p>"),
]
#-----------------------------------------------------------------------------------------------------
# getStudentbyQuery(f"SELECT * FROM SinhVien WHERE HoTen LIKE '%Trung%'")
#============================================================

sqlInsertnhommonan = """INSERT INTO NhomMonAn (MaNhom, TenNhom) VALUES (%s,%s)"""
valsss = [
  ('1', 'Khai vị'),
  ('2', 'Hải sản'),
  ('3', 'Bia - Nước ngọt'),
  ('4', 'Lẩu')
]

#=======================================================

def XuatMonAn():
    sql = "SELECT * FROM MonAn"
    try:
        for row in values_Of_Select(sql):
            tree.insert("", "end", values=(row[0], row[1], row[2],row[3],row[4]))
    except mysql.connector.Error as err:
        print("" + err)



# def Tim_Kiem(content:str, _table:str):
#     # Xoá dữ liệu hiện tại trong treeview
#     for row in tree.get_children():
#         tree.delete(row)
#     sql = f"SELECT * FROM {_table} Where TenNhom like '%{content}%'"
#     try:
#         for row in values_Of_Select(sql):
#             tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
#     except mysql.connector.Error as err:
#         print("" + err)

# def callback(var):
#    content= var.get()
#    Tim_Kiem(content, "MonAn")
# #Create an variable to store the user-input
# var = StringVar()
# var.trace("w", lambda name, index,mode, var=var: callback(var))

root = tk.Tk()
cbNhomMonAn = ttk.Combobox(root, width = 27) 
cbNhomMonAn.pack()
cbNhomMonAn['values'] = ('Khai vị',  
                          'Hải sản', 
                          'Bia - Nước ngọt', 
                          'Lẩu') 
columns = ("Mã sv", "Họ tên", "Lớp")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=250)
tree.pack()
XuatMonAn()
root.mainloop()

