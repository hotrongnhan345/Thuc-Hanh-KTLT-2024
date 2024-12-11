print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV:235752021610123")
class Nguoi:
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Khởi tạo đối tượng
aNam = Nam()
aNu = Nu()

# Gọi phương thức và in kết quả
print(aNam.getGender())
print(aNu.getGender())
