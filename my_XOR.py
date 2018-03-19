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

“””
itertools 模組提供了三個函數(類別class)用來產生一個無限序列反覆運算器：
count(firstval=0, step=1)
創建一個從 firstval (預設值為 0) 開始，以 step (預設值為 1) 為step的的無限整數反覆運算器

cycle(iterable)
對 iterable 中的元素反復執行迴圈，返回反覆運算器

repeat(object [,times]
反復生成 object，如果給定 times，則重複次數為 times，否則為無限
“””
