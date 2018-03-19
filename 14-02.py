from string import ascii_uppercase as uppercase
from itertools import cycle

#建立密碼表
table = dict()
for ch in uppercase:
    index = uppercase.index(ch)
    table[ch] = uppercase[index:]+uppercase[:index]

#建立解密密碼表
deTable = {'A':'A'}
start = 'Z'
for ch in uppercase[1:]:
    index = uppercase.index(ch)
    deTable[ch] = chr(ord(start)+1-index)

#解密金鑰
def deKey(key):
    return ''.join([deTable[i] for i in key])

#加密/解密
def encrypt(plainText, key):
    result = []
    #建立cycle物件，支援金鑰字母的循環使用
    currentKey = cycle(key)
    for ch in plainText:
        if 'A'<=ch<='Z':
            index = uppercase.index(ch)
            #取得金鑰字母
            ck = next(currentKey)
            result.append(table[ck][index])
        else:
            result.append(ch)
    return ''.join(result)

key = 'DONGFUGUO'
p = 'PYTHON 3.5.1 PYTHON 2.7.11'
c = encrypt(p, key)
print(p)
print(c)
print(encrypt(c,deKey(key)))
