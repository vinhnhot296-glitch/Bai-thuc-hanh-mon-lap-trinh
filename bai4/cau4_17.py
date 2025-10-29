def tong_uoc_so(x):
    tong = 1  # 1 luôn là ước của mọi số > 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            tong += i
            if i != x // i:
                tong += x // i
    return tong if x > 1 else 0

n = int(input("Nhập số nguyên n: "))
for num in range(1, n):
    if tong_uoc_so(num) > num:
        print(num, end=" ")

