print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import tkinter as tk

def ShowChoice():
    # In ra giá trị của lựa chọn hiện tại khi có sự thay đổi
    print(v.get())

# Khởi tạo cửa sổ chính
root = tk.Tk()

# Biến IntVar để lưu trữ giá trị của nút được chọn
v = tk.IntVar()
v.set(1) # Đặt giá trị mặc định ban đầu là 1 ("Python")

# Danh sách các ngôn ngữ lập trình và giá trị tương ứng
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Thêm nhãn hướng dẫn
tk.Label(root,
         text="Chọn ngôn ngữ lập trình yêu thích của bạn:",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các Radiobutton sử dụng vòng lặp
for val, language in enumerate(languages):
    tk.Radiobutton(root,
                   text=language,
                   # indicatoron=0 biến radio button thành nút nhấn
                   indicatoron=0,
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

# Chạy vòng lặp sự kiện chính
root.mainloop()
