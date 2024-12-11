print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
import tkinter as tk

# Tạo cửa sổ 1
root1 = tk.Tk()
menu1 = tk.Menu(root1)
root1.config(menu=menu1)

# Tạo menu "File" cho cửa sổ 1
filemenu1 = tk.Menu(menu1)
menu1.add_cascade(label="File", menu=filemenu1)
filemenu1.add_command(label="New")
filemenu1.add_command(label="Open")
filemenu1.add_separator()
filemenu1.add_command(label="Exit", command=root1.quit)

# Tạo cửa sổ 2
root2 = tk.Tk()
menu2 = tk.Menu(root2)
root2.config(menu=menu2)

# Tạo menu "File" và "Insert" cho cửa sổ 2
filemenu2 = tk.Menu(menu2)
insertmenu2 = tk.Menu(menu2)
menu2.add_cascade(label="File", menu=filemenu2)
menu2.add_cascade(label="Insert", menu=insertmenu2)
filemenu2.add_command(label="New")
filemenu2.add_command(label="Open")
insertmenu2.add_command(label="Text")
insertmenu2.add_command(label="Picture")

# Hiển thị các cửa sổ
root1.mainloop()
root2.mainloop()
