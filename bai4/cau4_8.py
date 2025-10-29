chuoi = input("Nhập dãy các từ (cách nhau bằng khoảng trắng): ").strip()
tu_list = chuoi.split()
max_len = max(len(tu) for tu in tu_list)
tu_dai_nhat = [tu for tu in tu_list if len(tu) == max_len]
print("Các từ dài nhất là:")
for tu in tu_dai_nhat:
    print("-", tu)
print("Độ dài:", max_len)
