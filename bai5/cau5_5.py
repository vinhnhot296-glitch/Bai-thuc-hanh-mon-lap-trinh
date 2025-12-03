print('họ tên: trần huy vinh; MSSV:245752021610007')
def sort_list(lst):
    """Sắp xếp danh sách theo thứ tự tăng dần."""
    return sorted(lst)

def find_max(lst):
    """Tìm phần tử lớn nhất trong danh sách."""
    return max(lst)

def find_min(lst):
    """Tìm phần tử nhỏ nhất trong danh sách."""
    return min(lst)

def main():
    try:
        n = int(input("Nhập số lượng phần tử của danh sách: "))
        lst = []
        for i in range(n):
            val = float(input(f"Nhập phần tử thứ {i+1}: "))
            lst.append(val)

        sorted_lst = sort_list(lst)
        max_val = find_max(lst)
        min_val = find_min(lst)

        print("\nKết quả:")
        print(f"- Danh sách sau khi sắp xếp: {sorted_lst}")
        print(f"- Phần tử lớn nhất: {max_val}")
        print(f"- Phần tử nhỏ nhất: {min_val}")
    except ValueError:
        print("⚠️ Vui lòng nhập số hợp lệ.")

if __name__ == "__main__":
    main()

