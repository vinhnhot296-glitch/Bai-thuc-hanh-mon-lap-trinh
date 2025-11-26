print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import tkinter as tk
from tkinter import messagebox

# ================== FORM A: THÔNG TIN CÁ NHÂN ==================
def create_personal_info_form():
    info_window = tk.Toplevel()
    info_window.title("Thông tin cá nhân")
    info_window.geometry("350x180")

    tk.Label(info_window, text="THÔNG TIN CÁ NHÂN",
             font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(info_window, text="Họ tên:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    tk.Label(info_window, text="Nguyễn Như Diệu").grid(row=1, column=1, sticky="w")

    tk.Label(info_window, text="Ngày sinh:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    tk.Label(info_window, text="02/01/2006").grid(row=2, column=1, sticky="w")

    tk.Label(info_window, text="MSSV:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    tk.Label(info_window, text="245752021610124").grid(row=3, column=1, sticky="w")

    tk.Label(info_window, text="Ngành học:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
    tk.Label(info_window, text="KTĐK & TĐH").grid(row=4, column=1, sticky="w")


# ================== FORM B: RADIO BUTTON ==================
def create_radio_form():
    radio_window = tk.Toplevel()
    radio_window.title("Radio Button Example")
    radio_window.geometry("300x250")

    radio_var = tk.IntVar(value=1)  # mặc định chọn số 1

    tk.Label(radio_window, text="WELCOME", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Các nút radio tương ứng với số 1,2,3
    tk.Radiobutton(radio_window, text="First", variable=radio_var, value=1,
                   font=("Arial", 12)).pack(anchor="w", padx=30)
    tk.Radiobutton(radio_window, text="Second", variable=radio_var, value=2,
                   font=("Arial", 12)).pack(anchor="w", padx=30)
    tk.Radiobutton(radio_window, text="Third", variable=radio_var, value=3,
                   font=("Arial", 12)).pack(anchor="w", padx=30)

    def on_click_me():
        selected = radio_var.get()
        messagebox.showinfo("Thông báo", f"Bạn đã chọn số: {selected}")

    tk.Button(radio_window, text="Click Me", font=("Arial", 12),
              command=on_click_me).pack(pady=20)


# ================== CỬA SỔ CHÍNH ==================
root = tk.Tk()
root.title("Chọn chức năng")
root.geometry("300x200")

tk.Label(root, text="CHỌN BÀI TẬP", font=("Arial", 14, "bold")).pack(pady=15)

# Nút mở form thông tin cá nhân
tk.Button(root, text="Form A: Thông tin cá nhân",
          font=("Arial", 12), width=25,
          command=create_personal_info_form).pack(pady=5)

# Nút mở form radio button
tk.Button(root, text="Form B: Radio Button",
          font=("Arial", 12), width=25,
          command=create_radio_form).pack(pady=5)

root.mainloop()

