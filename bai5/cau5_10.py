def bubbleSort(nlist):
    length = len(nlist)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
    return nlist

# Nhập danh sách từ bàn phím
if __name__ == "__main__":
    input_str = input("Nhập các số cách nhau bởi dấu phẩy: ")
    try:
        nlist = [int(x.strip()) for x in input_str.split(',')]
        sorted_list = bubbleSort(nlist)
        print("Danh sách sau khi sắp xếp:", sorted_list)
    except ValueError:
        print("Vui lòng chỉ nhập các số nguyên, cách nhau bởi dấu phẩy.")
