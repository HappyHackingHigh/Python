import string
import random
from Crypto.Cipher import AES

#產生指定長度的金鑰
def keyGenerater(length):
    if length not in (16, 24, 32):
        return None
    x = string.ascii_letters+string.digits
    return ''.join([random.choice(x) for i in range(length)]) 

def encryptor_decryptor(key, mode):
    return AES.new(key, mode, b'0000000000000000')

#以指定金鑰和模式加密給定的資料
def AESencrypt(key, mode, text):
    encryptor = encryptor_decryptor(key, mode)
    return encryptor.encrypt(text)

#以指定金鑰和模式解密給定的資料
def AESdecrypt(key, mode, text):
    decryptor = encryptor_decryptor(key, mode)
    return decryptor.decrypt(text)

if __name__ == '__main__':
    text = '山東省煙臺市 Python3.5 is excellent.'
    key = keyGenerater(16)
    #隨機選擇AES的模式
    mode = random.choice((AES.MODE_CBC, AES.MODE_CFB, AES.MODE_ECB, AES.MODE_OFB))
    if not key:
        print('Something is wrong.')
    else:
        print('key:', key)
        print('mode:', mode)
        print('Before encryption:', text)
        #明文必須是位元組字串形式，且長度為16的倍數
        text_encoded = text.encode()
        text_length = len(text_encoded)
        padding_length = 16 - text_length%16
        text_encoded = text_encoded + b'0'*padding_length        
        text_encrypted = AESencrypt(key, mode, text_encoded)
        print('After encryption:', text_encrypted)
        text_decrypted =AESdecrypt(key, mode, text_encrypted)
        print('After decryption:', text_decrypted.decode()[:-padding_length])
