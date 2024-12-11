print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        # Khởi tạo thuộc tính chiều dài và chiều rộng
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        # Tính diện tích hình chữ nhật
        return self.chieu_dai * self.chieu_rong

# Tạo một đối tượng Hinhchunhat với chiều dài 5 và chiều rộng 3
hcn = Hinhchunhat(5, 3)

# In ra diện tích của hình chữ nhật
print("Diện tích hình chữ nhật:", hcn.tinh_dien_tich())
