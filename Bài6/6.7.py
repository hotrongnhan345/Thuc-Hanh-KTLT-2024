print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV:235752021610123")
import math

class Circle:
    def __init__(self, radius):
        """
        Khởi tạo đối tượng Circle với bán kính.
        """
        self.radius = radius

    def area(self):
        """
        Tính diện tích của hình tròn.
        """
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """
        Tính chu vi của hình tròn.
        """
        return 2 * math.pi * self.radius
circle = Circle(5)  # Tạo hình tròn với bán kính 5
print("Diện tích:", circle.area())  # In diện tích
print("Chu vi:", circle.circumference())  # In chu vi
