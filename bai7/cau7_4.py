def file_read_from_head(fname, nlines):
    from itertools import islice
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            for line in islice(f, nlines):
                print(line.rstrip('\n')) 
                
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp '{fname}'. Vui lòng kiểm tra lại đường dẫn của 'test.txt'.")
