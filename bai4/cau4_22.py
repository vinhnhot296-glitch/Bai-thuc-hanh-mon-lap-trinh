def main():
    result = []
    for num in range(1000, 3001):  # từ 1000 đến 3000
        s = str(num)
        if all(int(ch) % 2 == 0 for ch in s):  # kiểm tra tất cả chữ số đều chẵn
            result.append(s)
    print(",".join(result))

if __name__ == "__main__":
    main()
