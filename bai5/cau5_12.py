import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sử dụng lexsort: sắp xếp theo height trước, nếu bằng thì theo id
# Lưu ý: thứ tự trong lexsort là (ưu tiên phụ, ưu tiên chính)
indices = np.lexsort((student_id, student_height))

# In chỉ số sắp xếp
print("Chỉ số:")
print(indices)

# In dữ liệu đã sắp xếp
print("\nDữ liệu sắp xếp:")
for i in indices:
    print(student_id[i], student_height[i])
