def main():
    # Nhập chuỗi số nhị phân, ví dụ: 0100,0011,1010,1001
    s = input("Nhập chuỗi số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")

    # Tách thành danh sách
    binaries = s.split(",")

    # Lọc các số chia hết cho 5
    result = [b for b in binaries if int(b, 2) % 5 == 0]

    # In ra kết quả
    print(",".join(result))

if __name__ == "__main__":
    main()
