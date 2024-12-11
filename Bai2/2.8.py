print("Sinh Viên: Hồ Trọng Nhân")
print("MSSV: 235752021610123")
a, b = 0, 1
total = 0
print(a, end="")
while b < 4000000:
    if b % 2 == 0:
        total += b
    a, b = b, a+b
    print(b, end="")
print("\nSum of even numbers term in Fibonacci series:", total)
