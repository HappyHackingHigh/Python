from hashlib import md5
from string import ascii_letters, digits
from itertools import permutations
from time import time

all_letters = ascii_letters + digits + '.,;'		#候選字元集

def decrypt_md5(md5_value):
    if len(md5_value) != 32:					#破解32位MD5值
        print('error')
        return
    
    md5_value = md5_value.lower()				#轉換為小寫MD5值
    
    for k in range(5,10):						#預期的密碼長度
        for item in permutations(all_letters, k):	#暴力測試
            item = ''.join(item)
            print('.', end='')					#顯示進度
            if md5(item.encode()).hexdigest() == md5_value:	#破解成功
                return item

md5_value = 'e7d057704ea5206d8cb61280741238f5'
start = time()
result = decrypt_md5(md5_value)
if result:
    print('\nSuccess:  '+md5_value+'==>'+result)
print('Time used:', time()-start)
