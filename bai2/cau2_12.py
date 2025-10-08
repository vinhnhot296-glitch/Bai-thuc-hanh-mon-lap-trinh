import re
passwords = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ").split(',')

valid_passwords = []

for p in passwords:
    p = p.strip()
    if (len(p) >= 6 and len(p) <= 12
        and re.search(r"[a-z]", p)
        and re.search(r"[A-Z]", p)
        and re.search(r"[0-9]", p)
        and re.search(r"[$#@]", p)):
        
        valid_passwords.append(p)
print(",".join(valid_passwords))
