#!/usr/bin/python3

info = '''
-------------双色球游戏-----------
1、玩家分别选取六个带数字的红球和两个带数字的篮球。
2、红球数字范围为1-30，篮球数字范围为50-55。
3、所选取的数字不可重复！
----------------End---------------
'''

print(info)

red_num = []

i = 0

while i < 6:
    red_num.append(int(input("[" + "%s" % (i + 1) + "] select red num : ")))
    if red_num[i] < 0 or red_num[i] > 30:
        print("The number is must in 1-30, you need to enter other number.")
        del red_num[i]
        continue
    elif red_num.count(red_num[i]) > 1:
        print("The number is exist, you need to enter other number.")
        del red_num[i]
        continue
    i += 1

blue_num = []

j = 0

while j < 2:
    blue_num.append(int(input("[" + "%s" % (j + 1) + "] select blue num : ")))
    if blue_num[j] < 50 or blue_num[j] > 55:
        print("The number is must in 50-55, you need to enter other number.")
        del blue_num[j]
        continue
    elif blue_num.count(blue_num[j]) > 1:
        print("The number is exist, you need to enter other number.")
        del blue_num[j]
        continue
    j += 1

print("\n")
print("The red numbers are : ", red_num)
print("The blue numbers are : ", blue_num)
print("Good luck.")
