import hashlib
import time

name = "张三"
birthday = "19900315"

# 当前时间戳
timestamp = str(int(time.time()))

# 拼接姓名、生日和时间戳
data = f"{name}{birthday}{timestamp}"

# 使用 MD5 取前 10 位
hash_result = hashlib.md5(data.encode()).hexdigest()[:10]
key = f"key{{{hash_result}}}"
print(key)  # 示例输出：key{d41d8cd98f}
