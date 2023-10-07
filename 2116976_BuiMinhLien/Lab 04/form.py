import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Entry

#window1s
window1 = tk.Tk()
window1.title("Hello")
window1.geometry("1280x720")

#containers
frame1 = Frame(window1)
frame2 = Frame(window1)
#widgets
""" label1 = ttk.Label(window1, text="Nhập họ tên", background="#fcec0c")
label2 = ttk.Label(window1, text="Nhập số điện thoại") """



""" Label(window1, text='First Name').grid(row=0)
Label(window1, text='Last Name').grid(row=1)
e1 = Entry(window1)
e2 = Entry(window1)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1) """

#organize
frame1.pack()
#run
window1.mainloop()
