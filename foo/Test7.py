# -*- codeing:utf-8 -*-
# 递归二分查询

a = [1,3,4,6,7,8,9,11,15,17,19,21,22,25,29,33,38,69,107,200]

def ret(a, n):
    mid = int(len(a) // 2) # 取中间数，即列表的中间索引
    if n > a[mid] and n < a[-1]: # 如果要查询的数大于中间数且小于最大值时
       a = a[mid:] # 将列表重新赋值，从中间值到最大值
       return ret(a, n) # 递归调用函数ret()
    elif n < a[mid] and n > a[0]: # 如果要查询的数大于最小值且小于中间值时
        a = a[:mid]
        return ret(a, n)
    elif n == a[mid]:
        print("该元素在列表中。")
    else:
        print("该元素不在列表中。")

ret(a, 31)
ret(a, 33)

