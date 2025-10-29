def main():
    s = input("Nhập câu: ")

    dem_hoa = 0
    dem_thuong = 0

    for ch in s:
        if ch.isupper():
            dem_hoa += 1
        elif ch.islower():
            dem_thuong += 1

    print("Chữ hoa:", dem_hoa)
    print("Chữ thường:", dem_thuong)

if __name__ == "__main__":
    main()
