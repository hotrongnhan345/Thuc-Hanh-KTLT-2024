print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
class Circle:
    def __init__(self, r):
        # Khởi tạo thuộc tính bán kính
        self.radius = r

    def area(self):
        # Tính diện tích hình tròn
        return self.radius**2 * 3.14

# Tạo một đối tượng Circle với bán kính là 2
aCircle = Circle(2)

# In ra diện tích của hình tròn
print(aCircle.area())
