import numpy as np

# Định nghĩa kiểu dữ liệu có cấu trúc
data_type = [('name', 'U10'), ('class', 'i4'), ('height', 'f4')]

# Dữ liệu đầu vào
students = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
student_array = np.array(students, dtype=data_type)

# Sắp xếp theo lớp, sau đó theo chiều cao
sorted_students = np.sort(student_array, order=['class', 'height'])

# In kết quả
print(sorted_students)
