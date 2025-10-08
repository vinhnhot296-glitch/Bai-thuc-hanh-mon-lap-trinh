import math

def Tinh(R):
    try:
        R = float(R)
        if R <= 0:
            print("Bán kính phải là một số dương lớn hơn 0.")
            return
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R ** 2
        print(f"Chu vi hình tròn là: {chu_vi:.2f}")
        print(f"Diện tích hình tròn là: {dien_tich:.2f}")
    except ValueError:  
        print("Giá trị nhập vào không hợp lệ. Vui lòng nhập một số.")

# Nhập bán kính từ bàn phím
ban_kinh = input("Nhập bán kính hình tròn: ")
Tinh(ban_kinh)
