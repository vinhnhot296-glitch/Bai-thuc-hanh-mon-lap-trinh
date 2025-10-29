def sort_list(lst):
    """Sắp xếp danh sách theo thứ tự tăng dần."""
    return sorted(lst)

def find_max(lst):
    """Tìm phần tử lớn nhất và vị trí của nó."""
    max_val = max(lst)
    max_index = lst.index(max_val)
    return max_val, max_index

def find_min(lst):
    """Tìm phần tử nhỏ nhất và vị trí của nó."""
    min_val = min(lst)
    min_index = lst.index(min_val)
    return min_val, min_index

# Gọi trực tiếp chương trình tại đây
print("=== CHƯƠNG TRÌNH TÌM PHẦN TỬ LỚN NHẤT VÀ NHỎ NHẤT TRONG DANH SÁCH ===")
try:
    n = int(input("Nhập số lượng phần tử của danh sách: "))
    lst = []
    for i in range(n):
        val = float(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(val)

    sorted_lst = sort_list(lst)
    max_val, max_index = find_max(lst)
    min_val, min_index = find_min(lst)

    print("\n📊 Kết quả:")
    print(f"- Danh sách sau khi sắp xếp: {sorted_lst}")
    print(f"- Phần tử lớn nhất: {max_val} (vị trí: {max_index})")
    print(f"- Phần tử nhỏ nhất: {min_val} (vị trí: {min_index})")
except ValueError:
    print("⚠️ Vui lòng nhập số hợp lệ.")
