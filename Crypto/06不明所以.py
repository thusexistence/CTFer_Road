ciphertext = "felhaagv{ewtehtehfilnakgw}"

# 提取奇数位字符（索引 0 开始，间隔 2）
decoded = ciphertext[0::2]
decoded2 = ciphertext[1::2]
print(decoded + decoded2)
