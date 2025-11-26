print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import turtle

colors = ["red", "green", "blue"]
painter = turtle.Turtle()
painter.pensize(3)
painter.speed(0)  # vẽ nhanh nhất

for i in range(12):     # 12 vòng tròn xoay đều 30 độ
    painter.pencolor(colors[i % 3])
    painter.circle(100)
    painter.right(30)   # xoay 30 độ để vòng tiếp theo lệch đi

turtle.done()
