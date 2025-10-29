
full_name = input("Nhập họ và tên : ").strip()
parts = full_name.split()
if len(parts) == 0:
    print("Bạn chưa nhập gì.")
elif len(parts) == 1:
    print("Vui lòng nhập cả họ và tên : ")
else:
    ho = parts[0]
    ten = parts[-1]
    print("Họ:", ho)
    print("Tên riêng:", ten)
