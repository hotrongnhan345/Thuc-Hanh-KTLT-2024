print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Khởi tạo biến để lưu trữ lựa chọn
v = tk.IntVar()
v.set(1)  # Mặc định chọn Python

# Danh sách các ngôn ngữ
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị lựa chọn đã chọn
def ShowChoice():
    print(f"Bạn đã chọn: {languages[v.get()-1][0]}")

# Tạo nhãn để hiển thị câu hỏi
tk.Label(root, 
         text="""Chọn ngôn ngữ lập trình yêu thích của bạn:""",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo các radio button
for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  variable=v,
                  value=val,
                  command=ShowChoice).pack(anchor=tk.W, padx=20)

# Hiển thị cửa sổ
root.mainloop()
