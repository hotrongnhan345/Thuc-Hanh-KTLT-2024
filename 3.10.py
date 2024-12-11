print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
import math

def tinh_hinh_tron(R):
    """Tính diện tích và chu vi hình tròn.

    Args:
        R: Bán kính hình tròn.

    Returns:
        Một tuple chứa diện tích và chu vi.
    """

    if R <= 0:
        print("Bán kính không hợp lệ")
        return None
    else:
        dien_tich = math.pi * R**2
        chu_vi = 2 * math.pi * R
        return dien_tich, chu_vi

# Nhập bán kính từ người dùng
R = float(input("Nhập bán kính hình tròn: "))

# Gọi hàm tính toán và in kết quả
ket_qua = tinh_hinh_tron(R)
if ket_qua:
    dien_tich, chu_vi = ket_qua
    print("Diện tích:", dien_tich)
    print("Chu vi:", chu_vi)
