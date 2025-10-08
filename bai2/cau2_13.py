print("Nguyễn Như Diệu")
print("MSV: 24575202160124")
import math
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
if a==0:
    if b==0:
        if c==0:
            print("phương trình vô số nghiệm")
        else:
            print("phương trình vô nghiệm")
    else:
        x = -c/b
        print("phương trình có một nghiệm duy nhất x=", x)
else:
    delta = b**2 -4*a*c
    if delta < 0:
        print("phương trình vô nghiệm")
    elif delta == 0:
        x= - b / (2*a)
        print("phương trình có nghiệm kép x1 = x2 = ", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("phương trình có 2 nghiệm phân biệt:")
        print("x1 = ", x1)
        print("x2 = ", x2)
