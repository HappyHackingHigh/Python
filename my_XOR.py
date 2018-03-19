#!/usr/bin/python 
# -*- coding: UTF-8 -*- 

def crypt(source, key):
    from itertools import cycle
    result = ''
    temp = cycle(key)
    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))
    return result

source = 'BreakALLCTF_IknowhowtoXORRRRing'
key = 'HappyHackingHigh'

print('未加密的明文:'+source)
encrypted = crypt(source, key)
print('加密過的密文:'+encrypted)
decrypted = crypt(encrypted, key)
print('解密過的答案:'+decrypted)
print('使用的金鑰:'+ key)


“””
itertools反覆運算器的特點是：惰性求值（Lazy evaluation）
只有當反覆運算至某個值時，它才會被計算
這個特點使得反覆運算器特別適合於遍歷大檔案或無限集合等
我們不用一次性將它們存儲在記憶體中。
“””
