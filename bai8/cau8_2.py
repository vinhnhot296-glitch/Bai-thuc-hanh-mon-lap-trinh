print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import turtle, random
colors = ["red","green","blue","orange","purple","pink","yellow"]#tạo danh sách màu
painter = turtle.Turtle()#tạo đối tượng vẽ
painter.pensize(3)#đặt độ dày nét

for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0, 0)
