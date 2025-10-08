def benefit(t, n, k):
    try:
        # Chuyển đổi các giá trị sang kiểu float để tính toán chính xác
        t = float(t)
        n = float(n)
        k = int(k)

        if t < 0 or n <= 0 or k <= 0:
            print("Vui lòng nhập lãi suất, số vốn và số tháng là các số hợp lệ.")
            return

        # Tính số tiền sau k tháng theo công thức lãi kép hàng tháng
        total = n * ((1 + t / 100) ** k)

        print(f"Số tiền nhận được sau {k} tháng là: {total:.2f} VND")
    except ValueError:
        print("Dữ liệu nhập vào không hợp lệ. Vui lòng nhập số.")

# Nhập dữ liệu từ bàn phím
t = input("Nhập lãi suất (%/tháng): ")
n = input("Nhập số vốn ban đầu (VND): ")
k = input("Nhập số tháng gửi: ")

benefit(t, n, k)
