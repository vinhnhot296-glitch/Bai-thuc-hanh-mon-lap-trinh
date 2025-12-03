print('họ tên: trần huy vinh; MSSV:245752021610007')
def main():
    s = input("Nhập câu: ")

    dem_chu = 0
    dem_so = 0

    for ch in s:
        if ch.isalpha():
            dem_chu += 1
        elif ch.isdigit():
            dem_so += 1

    print("Số chữ cái là:", dem_chu)
    print("Số chữ số là:", dem_so)

if __name__ == "__main__":
    main()

