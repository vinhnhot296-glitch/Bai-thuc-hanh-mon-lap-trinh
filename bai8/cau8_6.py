print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
from tkinter import *
from tkinter import messagebox
def NewFile():
    messagebox.showinfo("Thông báo", "New File!")
def OpenFile():
    messagebox.showinfo("Thông báo", "Open File!")
def ExitApp():
    root.quit()
def InsertTest():
    messagebox.showinfo("Thông báo", "Insert Test!")
def InsertPicture():
    messagebox.showinfo("Thông báo", "Insert Picture!")
def About():
    messagebox.showinfo("Về chúng tôi", "Đây là một ví dụ đơn giản về menu")
root = Tk()
root.title("tk")
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
#Menu file
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ExitApp)
# Menu Insert
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Test", command=InsertTest)
insertmenu.add_command(label="Picture", command=InsertPicture)
# Menu Help
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
# Thêm một nhãn trống để giữ bố cục
Label(root, text="").pack()
# Cấu hình cửa sổ chính để hiển thị
root.mainloop()
