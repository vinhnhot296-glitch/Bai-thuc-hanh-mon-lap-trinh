def Sequential_Search(dlist, item):
    for index in range(len(dlist)):
        if dlist[index] == item:
            return True, index
    return False, -1

# Chạy chương trình nếu file được thực thi trực tiếp
if __name__ == "__main__":
    try:
        # Nhập danh sách từ bàn phím
        input_str = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
        dlist = [int(x.strip()) for x in input_str.split(',')]

        # Nhập phần tử cần tìm
        item = int(input("Nhập giá trị cần tìm: "))

        # Gọi hàm tìm kiếm
        found, position = Sequential_Search(dlist, item)

        # In kết quả
        if found:
            print(f"Tìm thấy {item} tại vị trí {position}")
        else:
            print(f"Không tìm thấy {item} trong danh sách")
    except ValueError:
        print("Vui lòng nhập đúng định dạng số nguyên.")
