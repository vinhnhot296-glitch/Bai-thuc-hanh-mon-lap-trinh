import os

def file_read_from_tail(fname, lines):
    if not os.path.exists(fname):
        print(f"Tệp '{fname}' không tồn tại.")
        return

    bufsize = 8192
    fsize = os.stat(fname).st_size
    data = []
    iter = 0

    with open(fname, 'r') as f:
        while True:
            iter += 1
            seek_pos = max(fsize - bufsize * iter, 0)
            f.seek(seek_pos)
            data = f.readlines()
            if len(data) >= lines or seek_pos == 0:
                print(''.join(data[-lines:]))
                break
            
