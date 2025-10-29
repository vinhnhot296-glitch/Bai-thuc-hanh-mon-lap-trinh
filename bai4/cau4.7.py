s = input("Nhập chuỗi: ")
chuoi_moi = ""
for ch in s:
    if not ch.isdigit():
        chuoi_moi += ch
print("Chuỗi sau khi loại bỏ chữ số:", chuoi_moi)
