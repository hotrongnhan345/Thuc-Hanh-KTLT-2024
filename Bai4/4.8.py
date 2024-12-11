print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
def tim_tu_dai_nhat(chuoi):
    """Tìm từ dài nhất trong một chuỗi.

    Args:
        chuoi: Chuỗi cần tìm kiếm.

    Returns:
        Từ dài nhất trong chuỗi.
    """

    tu_dai_nhat = ""
    for tu in chuoi.split():
        if len(tu) > len(tu_dai_nhat):
            tu_dai_nhat = tu
    return tu_dai_nhat

# Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

# Gọi hàm và in kết quả
ket_qua = tim_tu_dai_nhat(chuoi)
print("Từ dài nhất:", ket_qua)
