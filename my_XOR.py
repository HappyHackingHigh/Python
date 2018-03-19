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
