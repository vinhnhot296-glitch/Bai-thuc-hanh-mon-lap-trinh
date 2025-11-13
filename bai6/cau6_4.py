class RomanToInteger:
    def __init__(self):
        # Tạo từ điển chứa giá trị của các ký tự La Mã
        self.roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, roman):
        total = 0
        prev_value = 0

        # Duyệt qua từng ký tự La Mã từ phải sang trái
        for ch in reversed(roman):
            value = self.roman_dict[ch]
            # Nếu giá trị nhỏ hơn giá trị trước đó thì trừ, ngược lại thì cộng
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total


# --- Chương trình chính ---
if __name__ == "__main__":
    converter = RomanToInteger()
    roman_num = input("Nhập số La Mã: ").upper()
    try:
        result = converter.roman_to_int(roman_num)
        print("Giá trị thập phân tương ứng là:", result)
    except KeyError:
        print("❌ Số La Mã không hợp lệ!")
