import numpy as np

# Định nghĩa kiểu dữ liệu cho từng trường
data_type = [('name', 'U20'), ('class', 'i4'), ('height', 'f4')]

# Dữ liệu mẫu
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

# In mảng ban đầu
print(" Mảng ban đầu:")
print(students)

# Sắp xếp theo chiều cao
sorted_students = np.sort(students, order='height')

# In kết quả đã sắp xếp
print("\n Mảng sau khi sắp xếp theo chiều cao:")
print(sorted_students)
