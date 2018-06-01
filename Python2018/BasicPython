一小時Python程式設計入門課

http://120.114.62.89

龍大大
=========================================
為什麼要學Python?
如何學Python?打造你的學習地圖!

=========================================
Python開發環境@windwos
下載python
安裝Python2.7==>裝在D:\python2
安裝Python3.6==>裝在D:\python3{記得改成python3}
-------------------------------------------------------
[1]使用python interactive shell
進入python
在cmd輸入python==>進入
離開==>exit()
-------------------------------------------------------
[2]使用notepad++寫程式==>記得檔名要XXX.py
執行:
[1]進入你的程式目錄 D:\p3code (三年級)  D:\p_code(一(年級) 
[2]D:\python2\python.exe XXX.py
或 D:\python3\python.exe XXX.py
-------------------------------------------------------
=========================================
Python開發環境@Ubuntu 16.04 LTS 64-bit

[1]使用python interactive shell
開啟terminal,輸入下列指令
python==>進入python 2.7shell
python3==>進入python 3.6.X shell
離開==>exit()
-------------------------------------------------------
[2]使用gedit(或nano或vim)寫程式==>記得檔名要XXX.py
python xxx.py
python3 xxx.py

=========================================
Python程式設計{基礎課程}

[1]輸入與輸出 USER INPUTS AND OUTPUTS:
[1.1]輸入:input | Raw_input
raw_input([prompt]) 函數從標準輸入讀取一個行，並返回一個字串（去掉結尾的分行符號）
input([prompt]) 函數和 raw_input([prompt]) 函數基本類似，但是 input 可以接收一個Python運算式作為輸入，並將運算結果返回。

------------------------------------------------

------------------------------------------------
#!/usr/bin/env python
#coding=utf-8

# radius = 20 # radius is now 20
# Prompt the user to enter a radius
radius = eval(input("Enter a number for radius: "))

# Compute area
area = radius * radius * 3.14159

# Display results
print("The area for the circle of radius", radius, "is", area)
------------------------------------------------

同時指定(Simultaneous Assignment )
------------------------------------------------
#!/usr/bin/env python
#coding=utf-8
# Prompt the user to enter three numbers
number1, number2, number3 = eval(input(
  "Enter three numbers separated by commas: "))

# Compute average
average = (number1 + number2 + number3) / 3

# Display result
print("The average of", number1, number2, number3,
    "is", average)
------------------------------------------------


[1.2]輸出:print
------------------------------------------------
[動手做]下列範例會產生何種結果
>>> q = 259
>>> p = 0.038
>>> print(q, p, p * q)
>>> print(q, p, p * q, sep=",")
>>> print(q, p, p * q, sep=" :-) ")
>>> print(str(q) + " " + str(p) + " " + str(p * q))
------------------------------------------------

[1.3]格式化輸出Formatted Output
[Further reading延伸閱讀]https://www.python-course.eu/python3_formatted_output.php

使用format()
"{0} love {1}......{2}".format("I","listening","classical Music")

使用%
'%c' % 97
'%c %c %c %c %c ' % (97,98,99,100,101)
'%d 八進位是%0 , 十六進位是  %x' % (97,97, 97)
 
 符  號	描述
      %c	 格式化字元及其ASCII碼
      %s	 格式化字串
      %d	 格式化整數
      %u	 格式化無符號整型
      %o	 格式化無符號八進位數
      %x	 格式化無符號十六進位數
      %X	 格式化無符號十六進位數（大寫）
      %f	 格式化浮點數字，可指定小數點後的精度
      %e	 用科學計數法格式化浮點數
      %E	 作用同%e，用科學計數法格式化浮點數
      %g	 %f和%e的簡寫
      %G	 %f 和 %E 的簡寫
      %p	 用十六進位數格式化變數的位址

[1.4]運算子
餘數運算子 (remainder|modulo)
------------------------------------------------
以秒表示的總時間長，取得分鐘數及剩餘的秒數。 
------------------------------------------------
#!/usr/bin/env python
#coding=utf-8

seconds = eval(input("Enter an integer for seconds: "))

minutes = seconds // 60     # Find minutes in seconds
remainingSeconds = seconds % 60   # Seconds remaining
print(seconds, "seconds is", minutes,  
  "minutes and", remainingSeconds, "seconds")
------------------------------------------------

[2]各種資料型態及其運算[1][2][3][4]...[X]

數字型(numeric)資料型態及其運算
字串(string)資料型態及其運算
列表|串列(list)資料型態及其運算
辭典|字典(dic)資料型態及其運算
………………

[3]迴圈與選擇
迴圈::while | for loop  |沒有do-while  |range|break|continue
-------------------------------------------------------
選擇:If |if-else| ..沒有switch

[3.1]選擇:If |if-else| ..沒有switch
-------------------------------------------------------
#猜數字游戲_版本一
#!/usr/bin/python
# -*- coding: UTF-8 -*-

number = 2315698

guess = int(raw_input('Enter an integer : '))

if guess == number:
  print 'Congratulations, you guessed it.' 
  print "(This is flag: BreakALL{It is easy to write if statement}!)" 
elif guess < number:
  print 'No, it is a little higher than that' 
  # You can do whatever you want in a block ...
else:
  print 'No, it is a little lower than that' 
  # you must have guess > number to reach here

print 'Done'

-------------------------------------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("")
print("西元年代對應到的十二生肖")
print("")
year = eval(input("請輸入你出生的年代: "))
print("")
zodiacYear = year % 12 
if zodiacYear == 0:
    print("monkey===猴子哩")
elif zodiacYear == 1:
    print("rooster雞")
elif zodiacYear == 2:
    print("dog狗狗")
elif zodiacYear == 3:
    print("pig豬豬")
elif zodiacYear == 4: 
    print("rat鼠")
elif zodiacYear == 5: 
    print("ox牛")
elif zodiacYear == 6:
    print("tiger虎虎生威")
elif zodiacYear == 7:
    print("rabbit兔子")
elif zodiacYear == 8:
    print("dragon偉大的龍")
elif zodiacYear == 9:
    print("snake蛇")
elif zodiacYear == 10:
    print("horse馬")
else: 
    print("sheep羊")
-------------------------------------------------------

[3.2]for loop

-------------------------------------------------------
words = ['cat', 'window', 'defenestrate']
for w in words:
   print w, len(w)
-------------------------------------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
-------------------------------------------------------
================================================================
【Python 練習實例81】
題目：809*??=800*??+9*?? 其中??代表的兩位數, 809*??為四位數，
8*??的結果為兩位數，9*??的結果為3位數。
求??代表的兩位數，及809*??後的結果。
================================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print b,' = 800 * ', i, ' + 9 * ', i
------------------------------------------------------------------



[3.3]while 迴圈

-------------------------------------------------------
#猜數字游戲_版本二:Python3
#!/usr/bin/env python
#coding=utf-8

from __future__ import print_function

import random

x = random.randint(1,100)

while (1):
   number = int(input("猜數字，輸入一個數字:"))
   if x == number:
      print("您猜對了!")
      print(“獎品是 BreakALL{you have done a good guess}")
      break
   elif x > number:
      print("比",number,"大")
   elif x < number:
      print("比",number,"小")


[程式開發作業]最大公因數

--------------------------------
[3.3]range
range(start, stop[, step])

[動手做]下列範例會產生何種結果
範例:range(100)
範例:range(1, 101)
範例:range(0, 10, 2)
範例:range(0, -10, -1)

>>>x = 'BreakALL'
>>> for i in range(len(x)) :
...     print(x[i])
--------------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
tmp = 0
for i in range(1,101):
    tmp += i
print 'The sum is %d' % tmp
--------------------------------
================================================================
【Python 練習實例30】
輸入一個5位數，判斷它是不是回文數。
12321是回文數，個位與萬位相同，十位與千位相同。
================================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
a = int(raw_input("請輸入一個數字:\n"))
x = str(a)
flag = True
 
for i in range(len(x)/2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print "%d 是一個回文數!" % a
else:
    print "%d 不是一個回文數!" % a
------------------------------------------------------------

--------------------------------
nested loop 巢狀迴圈
[程式開發作業]99乘法表



[4]函式/函數/function
函數是組織好的，可重複使用的，用來實現單一，或相關聯功能的程式碼片段。
函數能提高應用的模組性，和代碼的重複利用率。
Python提供了許多內建函數，比如print()。
使用者也可以自己創建函數，這被叫做使用者自訂函數。

定義一個函數
你可以定義一個由自己想要功能的函數，以下是簡單的規則：
函數代碼塊以 def 關鍵字開頭，後接函數識別字名稱和圓括號()。
任何傳入參數和引數必須放在圓括號中間。圓括號之間可以用於定義參數。
函數的第一行語句可以選擇性地使用文檔字串—用於存放函數說明。
函數內容以冒號起始，並且縮進。
return [運算式] 結束函數，選擇性地返回一個值給調用方。不帶運算式的return相當於返回 None。

語法
def functionname( parameters ):
   "函數_文檔字串"
   function_suite
   return [expression]

================================================================
【Python 練習實例47】練習撰寫函式swap(a,b)
寫一個函式將輸入的兩個變數值互換
================================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def swap(a,b):
    a,b = b,a
    return (a,b)
 
if __name__ == '__main__':
    x = 10
    y = 20
    print 'x = %d,y = %d' % (x,y)
    x,y = swap(x,y)
    print 'x = %d,y = %d' % (x,y)
---------------------------------------------------------

-----------------------------
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
-----------------------------

-----------------------------
[Further reading延伸閱讀]
http://python3-cookbook.readthedocs.io/zh_CN/latest/chapters/p07_functions.html
可接受任意數量參數的函數
只接受關鍵字參數的函數
給函數參數增加元資訊
返回多個值的函數
定義有預設參數的函數
定義匿名或內聯函數
匿名函數捕獲變數值
減少可調用物件的參數個數
將單方法的類轉換為函數
帶額外狀態資訊的回呼函數
內聯回呼函數
訪問閉包中定義的變數
-----------------------------
[4.2]遞迴函式==recursive vs iterative(loop)
[程式開發作業]費氏數列
[程式開發作業]n!
[程式開發作業]河內塔

=========================================
[程式開發作業]
費氏數列Fibonacci sequence:recursive vs iterative(loop)
又稱黃金分割數列
0、1、1、2、3、5、8、13、21、34、……。
在數學上，費波那契數列是以遞迴的方法來定義：
F(0) = 0     (n=0)
F(1) = 1    (n=1)
F(n) = F(n-1)+ F(n-2)(n=>2)
=========================================
-----------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
 
print fib(10)
-----------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print fib(10)
-----------------------------
================================================================
【Python 練習實例28】
有5個人坐在一起，
問第五個人多少歲？他說比第4個人大2歲。
問第4個人歲數，他說比第3個人大2歲。
問第三個人，又說比第2人大兩歲。
問第2個人，說比第一個人大兩歲。
最後問第一個人，他說是10歲。
請問第五個人多大？
================================================================


-----------------------------
[4.3]匿名函式及lambda運算式
-----------------------------

[4.4]python內建函式Built-in Functions:
https://docs.python.org/2/library/functions.html

dir(__builtins__)
help('math')
help(id)

import sys
print(system.builtin_module_names)
----------------------
Ascii code
https://zh.wikipedia.org/wiki/ASCII
ord('a')
chr(97)
chr(ord('A')+1)
----------------------

[4.5]使用函式來模組化程式
函式可用來減少多餘的程式碼，允許程式碼重複使用，還可以用來模組化程式碼，提升程式品質

步驟一:先將常用的功能寫成函式MyGCD.py
-----------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Return the gcd of two integers 
def gcd(n1, n2):
    gcd = 1 # Initial gcd is 1
    k = 2   # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # Update gcd
        k += 1

    return gcd # Return gcd

-----------------------------
步驟二:在主程式呼叫函式MyGCD.py
-----------------------------
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MyGCD import gcd # 載入要用的模組

# 請使用者輸入兩個整數
n1 = eval(input("請輸入第一個整數: "))
n2 = eval(input("請輸入第二個整數 "))

# 輸出兩個整數的最大公因數
print("兩個整數的最大公因數", n1,
    "and", n2, "is", gcd(n1, n2))
-----------------------------


[5]標準函式庫The Python Standard Library[1][2][3][4]5[6][7]
https://docs.python.org/2/library/index.html
無須安裝,但要import

binascii:
base64::是一種任意二進位到文本字串的編碼方法，常用於在URL、Cookie、網頁中傳輸少量二進位資料
    https://docs.python.org/2/library/base64.html#module-base64
hashlib::提供了常見的雜湊演算法，如MD5，SHA1

-------------------------------------
import time
import math

start = time.time()						#取得目前時間
for i in range(10000000):
    math.sin(i)
print('Time Used:', time.time()-start)	#輸出所耗時間
-------------------------------------
import hashlib

a = ‘HappyCTF{It is FUN hashing with python hashlib}’

print hashlib.md5(a).hexdigest()
print hashlib.sha1(a).hexdigest()
print hashlib.sha224(a).hexdigest()
print hashlib.sha256(a).hexdigest()
print hashlib.sha384(a).hexdigest()
print hashlib.sha512(a).hexdigest()
-------------------------------------
===============================================================================
Base64編碼與解碼
https://zh.wikipedia.org/wiki/Base64
===============================================================================
import base64
s = ‘FunnyCTF{BasE64 encoding is fufufufun!}'
a = base64.b64encode(s)
print a
print base64.b64decode(a)
c = base64.b32encode(s)
print c
print base64.b32decode(c)

===============================================================================
使用binascii — Convert between binary and ASCII
二進位|十進位|十六進位與ASCII互換的好模組
https://docs.python.org/2/library/binascii.html

binascii.b2a_hex(data)    ||     binascii.hexlify(data)
Return the hexadecimal representation of the binary data. 
Every byte of data is converted into the corresponding 2-digit hex representation. 
The resulting string is therefore twice as long as the length of data.

binascii.a2b_hex(hexstr)  ||  binascii.unhexlify(hexstr)
Return the binary data represented by the hexadecimal string hexstr. 
This function is the inverse of b2a_hex(). 
hexstr must contain an even number of hexadecimal digits 
(which can be upper or lower case), otherwise a TypeError is raised.
===============================================================================

#coding:utf-8
import binascii
a = ‘HappyCTF{Useful tools binascii}'
b = binascii.b2a_hex(a)
print b
print binascii.a2b_hex(b)
c = binascii.hexlify(a)
print c
print binascii.unhexlify(c)
-------------------------------------

[6]第三方模組[1][2][3][4]5[6][7]......[X]
需要安裝,也要import

PyPI - the Python Package Index
https://pypi.python.org/pypi
-------------------------------------
安裝模組:
pip list
pip install XXXXX
pip uninstall XXXXX
pip install --upgrade XXXX  #升級模組
-------------------------------------
pycrypto
pycrypto 2.6.1
Cryptographic modules for Python.


[7]各種類型檔案存取[1][2][3][4]5[6][7]

=============================================
【Python 練習範例98】
從鍵盤輸入一個字串，將小寫字母全部轉換成大寫字母，
然後輸出到一個檔"test"中保存。
Python 2.7:OK
Python 3.6
=============================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    fp = open('test.txt','w')
    string = raw_input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt','r')
    print fp.read()
    fp.close()

=============================================
if __name__ == '__main__' 如何正确理解?
https://www.zhihu.com/question/49136398
=============================================

=============================================
參考資料:
[1]Python Cookbook 3rd Edition Documentation
http://python3-cookbook.readthedocs.io/zh_CN/latest/index.html

[2]
https://www.python-course.eu/python3_modules_and_modular_programming.php

[3]Python Documentation contents
https://docs.python.org/3/contents.html
https://docs.python.org/2/contents.html

[5]Python Essential Reference, 5th Edition
https://forum.dabeaz.com/t/python-essential-reference-5th-edition/145
