# Nhập chuỗi số nhị phân từ bàn phím
s = input("Nhập chuỗi số nhị phân, cách nhau bởi dấu phẩy: ")

# Tách chuỗi thành danh sách
binaries = s.split(",")

# In ra từng giá trị
for b in binaries:
    print(b)
