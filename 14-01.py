def KaiSaEncrypt(ch, k):
    if (not isinstance(ch, str)) or len(ch)!=1:
        print('The first parameter must be a character')
        return
    if (not isinstance(k, int)) or (not 1<=k<=25):
        print('The second parameter must be an integer between 1 and 25')
        return
    #把英文字母轉換為後面第k個字母
    if 'a'<=ch<=chr(ord('z')-k):
        return chr(ord(ch)+k)
    #把英文字母首尾相連
    elif chr(ord('z')-k)<ch<='z':
        return chr((ord(ch)-ord('a')+k)%26+ord('a'))
    elif 'A'<=ch<=chr(ord('Z')-k):
        return chr(ord(ch)+k)
    elif chr(ord('Z')-k)<ch<='Z':
        return chr((ord(ch)-ord('A')+k)%26+ord('A'))
    else:
        return ch

def encrypt(plain, k):
    return ''.join([KaiSaEncrypt(ch, k) for ch in plain])

def KaiSaDecrypt(ch, k):
    if (not isinstance(ch, str)) or len(ch)!=1:
        print('The first parameter must be a character')
        return
    if (not isinstance(k, int)) or (not 1<=k<=25):
        print('The second parameter must be an integer between 1 and 25')
        return
    #把英文字母首尾相連，然後將每個字母轉換為前面第k個字母
    if chr(ord('a')+k)<=ch<='z':
        return chr(ord(ch)-k)
    elif 'a'<=ch<chr(ord('a')+k):
        return chr((ord(ch)-k+26))
    elif chr(ord('A')+k)<=ch<='Z':
        return chr(ord(ch)-k)
    elif 'A'<=ch<chr(ord('A')+k):
        return chr((ord(ch)-k+26))
    else:
        return ch

def decrypt(plain, k):
    return ''.join([KaiSaDecrypt(ch, k) for ch in plain])

plainText = 'Explicit is better than implicit.'
cipherText = encrypt(plainText, 5)
print(plainText)
print(cipherText)
print(decrypt(cipherText,5))
