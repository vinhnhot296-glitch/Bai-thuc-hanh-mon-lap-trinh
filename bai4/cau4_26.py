def main():
    balance = 0
    while True:
        try:
            line = input().strip()
            if not line:   # nếu dòng trống thì dừng
                break
            parts = line.split()
            if len(parts) != 2:
                continue
            action, amount = parts[0], int(parts[1])
            if action == 'D':
                balance += amount
            elif action == 'W':
                balance -= amount
        except EOFError:
            break
    print(balance)

if __name__ == "__main__":
    main()
