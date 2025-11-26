def read_full_file_best(filename):
    """Đọc toàn bộ nội dung của tệp bằng with open."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"--- Nội dung tệp '{filename}' ---")
            print(content)
            return content
            
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp '{filename}'.")
    except Exception as e:
        print(f"Lỗi không xác định: {e}")
read_full_file_best('a.txt')
