print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
def get_sum(*num):
    tmp = 0
    for i in num:
        tmp +=1
    return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)
