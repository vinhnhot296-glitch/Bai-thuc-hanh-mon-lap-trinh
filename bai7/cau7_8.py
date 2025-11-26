def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')

# Ví dụ sử dụng
my_list = ['Python', 'Java', 'C++', 'JavaScript']
write_list_to_file('languages.txt', my_list)
print("Đã ghi danh sách vào tệp 'languages.txt'")
