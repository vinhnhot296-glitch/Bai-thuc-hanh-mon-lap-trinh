import math

# Vị trí ban đầu của robot
pos = [0, 0]

print("Nhập hướng di chuyển (UP/DOWN/LEFT/RIGHT và số bước).")
print("Nhấn Enter khi nhập xong để kết thúc:")

while True:
    s = input()
    if not s:  # nếu dòng trống -> thoát
        break
    movement = s.split()  # tách hướng và số bước
    direction = movement[0].upper()  # chuyển về chữ in hoa để tránh sai
    steps = int(movement[1])

    # Xử lý hướng di chuyển
    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps

# Tính khoảng cách từ gốc (0,0)
distance = math.sqrt(pos[0]**2 + pos[1]**2)
print("Khoảng cách là:", round(distance))
