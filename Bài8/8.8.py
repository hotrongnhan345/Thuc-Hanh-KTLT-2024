print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin cá nhân")

# Tạo các nhãn và ô nhập liệu
label_hoten = tk.Label(root, text="Họ tên:")
entry_hoten = tk.Entry(root)
label_ngaysinh = tk.Label(root, text="Ngày sinh:")
entry_ngaysinh = tk.Entry(root)
label_mssv = tk.Label(root, text="MSSV:")
entry_mssv = tk.Entry(root)
label_nganhhoc = tk.Label(root, text="Ngành học:")
entry_nganhhoc = tk.Entry(root)

# Đặt các widget lên cửa sổ
label_hoten.pack()
entry_hoten.pack()
label_ngaysinh.pack()
entry_ngaysinh.pack()
label_mssv.pack()
entry_mssv.pack()
label_nganhhoc.pack()
entry_nganhhoc.pack()

# Hiển thị cửa sổ
root.mainloop()
