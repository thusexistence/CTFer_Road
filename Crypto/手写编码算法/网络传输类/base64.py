basecoding_mappinglist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def Base64(cipher_text):
    # 将输入转为二进制表示
    binary_format_text = ''.join(f'{byte:08b}' for byte in cipher_text)

    # 初始化结果
    index = 0
    base64str = ''

    # 每 24 位为一组处理
    while index < len(binary_format_text):
        bitarray = binary_format_text[index:index + 24]  # 提取 24 位
        index += 24

        # 如果不足 24 位，补齐 0
        if len(bitarray) < 24:
            bitarray = bitarray.ljust(24, '0')
        print(bitarray)
        # 每 6 位分割，映射到 Base64 表
        for i in range(0, len(bitarray), 6):
            bits_pattern = bitarray[i:i + 6]
            base64str += basecoding_mappinglist[int(bits_pattern, 2)]

    # 计算填充的 "=" 个数
    padding_length = (3 - len(cipher_text) % 3) % 3
    base64str += '=' * padding_length

    return base64str


# 示例
binary_data = input('输入要编码的数据: ')
print('BASE64 编码结果:', Base64(binary_data.encode('UTF-8')))
