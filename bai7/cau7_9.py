import os

def copy_file(source_file, destination_file):
    if not os.path.exists(source_file):
        print(f"Tệp nguồn '{source_file}' không tồn tại.")
        return
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print(f"Đã sao chép nội dung từ '{source_file}' sang '{destination_file}'.")
    
