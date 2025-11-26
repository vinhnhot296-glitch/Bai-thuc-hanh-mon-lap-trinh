print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import tkinter as tk
root = tk.Tk()
root.title("Thông tin cá nhân")
root.geometry("350x180")

tk.Label(root, text="THÔNG TIN CÁ NHÂN",
         font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Họ tên:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="Nguyễn Như Diệu").grid(row=1, column=1, sticky="w")

tk.Label(root, text="Ngày sinh:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="02/01/2006").grid(row=2, column=1, sticky="w")

tk.Label(root, text="MSSV:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="245752021610124").grid(row=3, column=1, sticky="w")

tk.Label(root, text="Ngành học:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
tk.Label(root, text="KTĐK & TĐH").grid(row=4, column=1, sticky="w")

root.mainloop()
