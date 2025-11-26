print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
from tkinter import *

# a) Xây dựng cửa sổ đồ họa window form
window = Tk()
window.title("Demo Tkinter")
window.geometry('350x200')

# Tạo Label
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# c) Xây dựng phương thức xử lý sự kiện khi bấm phím
def clicked():
    lbl.configure(text="Button was clicked !!!")

# b + d) Thêm Button vào window form và đổi màu nền (bg) + màu chữ (fg)
btn = Button(window, text="Click Me", command=clicked, bg="yellow", fg="blue")
btn.grid(column=1, row=0)

window.mainloop()
