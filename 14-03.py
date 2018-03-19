def encrypt(plainText, t):
    result = []
    length = len(t)
    #將明文分組
    temp = [plainText[i:i+length] for i in range(0,len(plainText),length)]
    #除最後一組之外的其他組進行換位處理
    for item in temp[:-1]:
        newItem = ''
        for i in t:
            newItem = newItem+item[i-1]
        result.append(newItem)
    return ''.join(result)+temp[-1]

p = 'Errors should never pass silently.'
#加密
c = encrypt(p, (1, 4, 3, 2))
print(c)
#解密
print(encrypt(c, (1, 4, 3, 2)))
