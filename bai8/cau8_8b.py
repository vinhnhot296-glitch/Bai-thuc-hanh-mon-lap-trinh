print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("350x250")

tk.Label(root, text="WELCOME", font=("Helvetica", 16, "bold")).pack(pady=10)

radio_var = tk.IntVar(value=1)


info_dict = {
    1: "Bạn đã chọn: First\nMô tả: Lựa chọn số 1",
    2: "Bạn đã chọn: Second\nMô tả: Lựa chọn số 2",
    3: "Bạn đã chọn: Third\nMô tả: Lựa chọn số 3"
}

tk.Radiobutton(root, text="First", variable=radio_var, value=1,
               font=("Arial", 12)).pack(anchor="w", padx=30)
tk.Radiobutton(root, text="Second", variable=radio_var, value=2,
               font=("Arial", 12)).pack(anchor="w", padx=30)
tk.Radiobutton(root, text="Third", variable=radio_var, value=3,
               font=("Arial", 12)).pack(anchor="w", padx=30)

def on_click_me():
    selected = radio_var.get()
    messagebox.showinfo("Thông báo", info_dict[selected])

tk.Button(root, text="Click Me", font=("Arial", 12),
          command=on_click_me).pack(pady=20)

root.mainloop()


