ds = input("Nhập các phần tử của list (cách nhau bằng khoảng trắng): ").split()
print("\nList ban đầu:", ds)
tim = input("\nNhập phần tử muốn tìm kiếm: ")
if tim in ds:
    print(f"Phần tử '{tim}' có trong list, ở vị trí thứ {ds.index(tim)}.")
else:
    print(f"Phần tử '{tim}' không có trong list.")
