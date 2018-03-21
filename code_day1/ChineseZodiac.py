#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
