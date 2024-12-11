print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
chuoi = input("Nhập chuỗi: ")
chuoi_moi = ""
for ky_tu in chuoi:
    if not ky_tu.isdigit():
        chuoi_moi += ky_tu
print(chuoi_moi)
