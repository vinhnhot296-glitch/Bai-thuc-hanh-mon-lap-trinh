def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Chạy chương trình nếu file được thực thi trực tiếp
if __name__ == "__main__":
    try:
        # Nhập danh sách và chuyển sang số nguyên
        input_str = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
        arr = [int(x.strip()) for x in input_str.split(',')]
        arr.sort()  # Sắp xếp danh sách trước khi tìm kiếm nhị phân

        # Nhập giá trị cần tìm
        value = int(input("Nhập giá trị cần tìm: "))

        # Gọi hàm tìm kiếm
        found = binary_search(arr, value)
        print("Kết quả tìm kiếm:", found)
    except ValueError:
        print("Vui lòng nhập đúng định dạng số nguyên.")
