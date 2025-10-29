def fibonacci_list(n):
    fib = [0, 1]
    while True:
        next_num = fib[-1] + fib[-2]
        if next_num >= n:
            break
        fib.append(next_num)
    return fib

# Nhập n
n = int(input("Nhập số nguyên n: "))

# Tạo list Fibonacci nhỏ hơn n
result = fibonacci_list(n)

# In ra màn hình
print(result)
