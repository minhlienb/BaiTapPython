import tkinter
from PIL import Image, ImageTk  
from tkinter import *

""" def open_new_window():
    extended_window = tkinter.Toplevel(main_window)
    extended_window.geometry("1280x720")
    extended_window.title = 'Cửa sổ mở rộng'
    main_window.withdraw() """

main_window = Tk(className='A window')
main_window.geometry("500x200")
button1 = tkinter.Button(main_window, text='new Window', width=25, command= main_window.destroy)
button1.pack()
main_window.mainloop() 

