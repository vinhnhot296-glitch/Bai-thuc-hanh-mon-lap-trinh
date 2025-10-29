# Nhập dãy số từ bàn phím, cách nhau bởi dấu phẩy
s = input("Nhập dãy số (cách nhau bởi dấu phẩy): ")

# Chuyển thành danh sách số nguyên
numbers = [int(x) for x in s.split(",")]

# Lọc số lẻ
odd_numbers = [x for x in numbers if x % 2 != 0]

# In ra kết quả, cách nhau bởi dấu phẩy
print(",".join(str(x) for x in odd_numbers))
