ds = input("Nhập các phần tử của list (cách nhau bằng khoảng trắng): ").split()
print("\nList ban đầu:", ds)
xoa = input("nhập phần tử muốn xoá: ")
if xoa in ds:
    ds.remove(xoa)
    print("list sau khi xoá phần tử",ds)
else:
    print("phần tử không tồn tại trong list.")
