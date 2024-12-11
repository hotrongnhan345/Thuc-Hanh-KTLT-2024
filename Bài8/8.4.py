print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")
#Thêm nhãn
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
#Xác định chức năng của nút
def clicked():
    def clicked():
    lbl.configure(text="Button was clicked!!!")

#Thêm nút
    btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)


