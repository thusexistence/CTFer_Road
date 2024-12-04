import libnum
s_box = 'qwertyuiopasdfghjkzxcvb123456#$'
s = 'u#k4ggia61egegzjuqz12jhfspfkay'
for k in range(30):
    b1 = k
for i in s[::-1]:
    b1 = b1*31 +s_box.index(i)
print(libnum.n2s(int(b1)))