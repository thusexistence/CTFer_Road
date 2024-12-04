def caesar_decrypt(text, shift):
    decrypted = ''
    for char in text:
        if char.isalpha():  # 仅对字母操作
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char  # 保留符号
    return decrypted

text = "73E-30U1&>V-H965S95]I<U]P;W=E<GT`"
for shift in range(26):  # 尝试所有位移量
    print(f"Shift {shift}: {caesar_decrypt(text, shift)}")
