print('họ tên: Nguyễn Như Diệu; MSSV:245752021610124')
import tkinter
import random

# list of possible colours  
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
timeleft = 120   # 🔥 Đã đổi thành 120 giây

# hàm bắt đầu game
def startGame(event):
    global timeleft
    if timeleft == 120:
        countdown()
    nextColour()

# hàm chọn màu tiếp theo
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # kiểm tra đúng – sai
        if e.get().lower() == colours[1].lower():
            score += 2       # 🔥 đúng +2
        elif e.get() != "":
            score -= 1       # 🔥 sai -1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # hiển thị chữ và màu
        label.config(fg=colours[1], text=colours[0])

        scoreLabel.config(text="Score: " + str(score))

# hàm đếm ngược
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


# ---------------- GUI -------------------

root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("400x250")

instructions = tkinter.Label(root,
    text="Type the COLOR of the text, not the word!",
    font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root,
    text="Press Enter to start",
    font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root,
    text="Time left: " + str(timeleft),
    font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()
