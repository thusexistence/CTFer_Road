def modified_caesar_decrypt(ciphertext):
    result = []
    base_shift = 5  # 初始偏移量
    for i, char in enumerate(ciphertext):
        if i == len(ciphertext) - 1:  # 最后一个字符偏移量固定为 26
            shift = 26
        else:
            shift = base_shift + i  # 偏移量递增
        result.append(chr(ord(char) + shift))
    return ''.join(result)

# 示例
ciphertext = "afZ_r9VYfScOeO_UL^RWUc"
plaintext = modified_caesar_decrypt(ciphertext)
print(plaintext)
