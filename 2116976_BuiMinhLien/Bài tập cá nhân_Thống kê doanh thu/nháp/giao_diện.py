import tkinter as tk
from tkinter import ttk
import mysql.connector

# Kết nối đến cơ sở dữ liệu [MySQL](https://www.google.com/search?q=MySQL)
# db = mysql.connector.connect(
#     host="your_host",
#     user="your_username",
#     password="your_password",
#     database="your_database"
# )

# Tạo cửa sổ [Tkinter](https://www.google.com/search?q=Tkinter)
window = tk.Tk()
window.title("Thông tin [Hàng Hóa](https://www.google.com/search?q=H%C3%A0ng%20H%C3%B3a)")

# Tạo [Treeview](https://www.google.com/search?q=Treeview)
tree = ttk.Treeview(window, columns=("MaHang", "TenHang", "Gia"))
tree.heading("#0", text="STT")
tree.heading("MaHang", text="Mã Hàng")
tree.heading("TenHang", text="Tên Hàng")
tree.heading("Gia", text="Giá")

# Hàm để hiển thị dữ liệu từ câu truy vấn SQL vào [Treeview](https://www.google.com/search?q=Treeview)
# def show_data():
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM [HangHoa](https://www.google.com/search?q=HangHoa)")
#     rows = cursor.fetchall()
    
#     # Xóa dữ liệu cũ trong [Treeview](https://www.google.com/search?q=Treeview)
#     tree.delete(*tree.get_children())
    
#     # Hiển thị dữ liệu mới từ câu truy vấn SQL
#     for i, row in enumerate(rows, start=1):
#         tree.insert("", "end", text=str(i), values=row)

# Button để hiển thị dữ liệu
btn_show = ttk.Button(window, text="Hiển thị dữ liệu")

# [Label](https://www.google.com/search?q=Label) và [Select Box](https://www.google.com/search?q=Select%20Box)
lbl_select = ttk.Label(window, text="Chọn một lựa chọn:")
select_box = ttk.Combobox(window, values=["Lựa chọn 1", "Lựa chọn 2", "Lựa chọn 3"])

# Định vị các phần tử trong giao diện
tree.pack()
btn_show.pack()
lbl_select.pack()
select_box.pack()

# Chạy giao diện
window.mainloop()