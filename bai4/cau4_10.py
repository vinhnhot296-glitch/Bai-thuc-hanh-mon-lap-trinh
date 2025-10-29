lst = input("Nhập các phần tử của list (cách nhau bằng khoảng trắng): ").split()
print("\nList ban đầu:", lst)
if len(lst) > 2:
    cat_list = lst[1:-1]
else:
    cat_list = []
print("List sau khi cắt (bỏ phần tử đầu và cuối):", cat_list)
