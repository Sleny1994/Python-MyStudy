# -*- coding:utf-8 -*-

# 1.写函数，计算传入数字参数的和。（动态传参）
# def add(x, y):
#     sum = x + y
#     print(sum)
#     # return sum
# add(3, 5)



# 2.写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
# import os
# def mod(filename, old_str, new_str):
#     tmp_file = "tmp_txt"
#     f = open(filename, "r+")
#     f_new = open(tmp_file, "w")
#     for lines in f:
#         if old_str in lines:
#             lines = lines.replace(old_str, new_str) 
#             # 此处不能使用strip对字符串lines做处理，否则换行符会被处理掉，最终输出的结果就不会换行
#         f_new.write(lines)
#     f.close()
#     f_new.close()
#     os.replace(tmp_file, filename)
#     print("修改成功")
# mod("test", "h", "H")



# 3.写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
# def check_isempty(*args):
#     if all(args) == False:
#         print("该对象内有空内容！")
#     else:
#         print(args)
# check_isempty((1,2),{0,1,2,3},"str",[])
# check_isempty((1,2),{0,1,2,3},"str")



# 4.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容（对value的值进行截断）,
#   并将新内容返回给调用者，注意传入的数据可以是字符、list、dict
# def func(dic):
#     list = dic.items()
#     for key, value in list:
#         if len(value) > 2:
#             value = value[:2]
#         new_dic = {key : value}
#         dic.update(new_dic)
#     return print(dic)  
# dic = {"1":"He", "2":[1,2,3,4,5], "3":"String"}
# func(dic)



# 5.解释闭包的概念
# def outer():
#     print("I'm outside.")
#     def inner():
#         print("I'm inside.")
#         return 0
#     return inner
# outer = outer()
# print(outer)
# print(outer())



# 6.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
#   例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃A’)]
# def puke():
#     list = []
#     huase = ['方块', '红桃', '黑桃', '梅花']
#     value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#     for i_hs in huase:
#         for i_va in value:
#             tuple = (i_hs, i_va) 
#             list.append(tuple)
#     print(list)
# puke()



# 7.写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# def max_min(*args):
#     args_list = list(args)
#     args_list.sort()
#     max = args_list[-1]
#     min = args_list[0]
#     key1 = "max"
#     value1 = max
#     key2 = "min"
#     value2 = min
#     dict = {key1:value1, key2:value2}
#     print(dict)
# max_min(8,1,2,5,3,7)



# 8.写函数，专门计算图形的面积
#   其中嵌套函数，计算圆的面积，正方形的面积和长方形的面积
#   调用函数area(‘圆形’,圆半径) 返回圆的面积
#   调用函数area(‘正方形’,边长) 返回正方形的面积
#   调用函数area(‘长方形’,长，宽) 返回长方形的面积
# def area(*args):
#     list_args = list(args)
#     def rec_area():
#         n = list_args[1]
#         m = list_args[2]
#         _area = n * m
#         print(_area)
#         return rec_area
#     def squ_area():
#         a = list_args[1]
#         _area = a ** 2 
#         print(_area)
#         return squ_area
#     def cir_area():
#         r = list_args[1]
#         _area = 3.14 * (r ** 2)
#         print(_area)
#         return cir_area
#     if "长方形" in args:
#         rec_area()
#     elif "正方形" in args:
#         squ_area()
#     else:
#         cir_area()
# area('圆形', 5)
# area('正方形', 5)
# area('长方形', 2, 3)



# 9.写函数，传入一个参数n，返回n的阶乘
# def cal(n):
#     j = 1
#     for i in range(1, n):
#         j = j * (i + 1)
#     print(j)
# cal(7)



# 10.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码



# 11.生成器和迭代器的区别？



# 12.生成器有几种方式获取value？
# 1）使用for循环输出 2）使用next()函数一个个输出



# 13.通过生成器写一个日志调用方法， 支持以下功能
#    根据指令向屏幕输出日志
#    根据指令向文件输出日志
#    根据指令同时向文件&屏幕输出日志
#    以上日志格式如下
#    2017-10-19 22:07:38 [1] test log db backup 3
#    2017-10-19 22:07:40 [2] user alex login success
#注意：其中[1],[2]是指自日志方法第几次调用，每调用一次输出一条日志
# import time
# def logger(filename, channel):
#     """
#     日志方法
#     :param filename: log filename
#     :param channel: 输出的目的地，屏幕(terminal)，文件(file)，屏幕+文件(both)
#     :return:
#     """
#     while True:
#         count = 0
#         if channel == 'terminal':
#             count += 1
#             output = yield
#             print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + ' [' + str(count) + '] ' + output)
#         elif channel == 'file':
#         elif channel == 'both':
# log_obj = logger("web.log", "terminal")
# log_obj.__next__()
# log_obj.send('user alex login success')



# 14.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# def func():
#     name = ['alex','wupeiqi','yuanhao','nezha']
#     new_name = []
#     for s in name:
#         s = s + '_sb'
#         new_name.append(s)
#     print(new_name)
# func()
# name = ['alex','wupeiqi','yuanhao','nezha']
# new_name = []
# for i in map(lambda name : str(name) + '_sb', name):
#     new_name.append(i)
# print(new_name)



# 15.用filter函数处理数字列表，将列表中所有的偶数筛选出来
# num = [1,3,5,6,7,8]
# new_list = []
# def is_o(n):
#     return n % 2 == 0
# for new_num in filter(is_o, num):
#     new_list.append(new_num)
# print(new_list)



# 16.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# 通过哪个内置函数可以计算购买每支股票的总价 -- sum()
# 用filter过滤出，单价大于100的股票有哪些
# def func():
#     for dic in portfolio:
#         # print(dic)
#         if dic['price'] > 100:
#             print(dic)
# func()
# s = filter(lambda dic : dic['price'] > 100, portfolio)
# for s in s:
#     print(s)



# 17.有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘alen’], 请将以字母“a”开头的元素的首字母改为大写字母；
# li = ['alex', 'egon', 'smith', 'pizza', 'alen']
# new_li = []
# for lines in li:
#     # print(lines)
#     if 'a' in lines[0]:
#         lines = lines.capitalize()
#     new_li.append(lines)
# print(new_li)



# 18.有列表 li = [‘alex’, ‘egon’, ‘smith’, ‘pizza’, ‘axen’], 请以列表中每个元素的第二个字母倒序排序；
# li = ['alex', 'egon', 'smith', 'pizza', 'axen']
# new_li = []
# new3_li = []
# for i in li:
#     li_two = map(ord, i[1])
#     for n_i in li_two:
#         new_li.append(n_i)
# new2_li = new_li.copy()
# # print(new2_li)
# new_li.sort(reverse=True)
# # print(new_li)
# for j in new_li:
#     new3_li.append(li[new2_li.index(j)])
# print(new3_li)



# 19.有名为poetry.txt的文件，其内容如下，请删除第三行；
# 昔人已乘黄鹤去，此地空余黄鹤楼。
# 黄鹤一去不复返，白云千载空悠悠。
# 晴川历历汉阳树，芳草萋萋鹦鹉洲。
# 日暮乡关何处是？烟波江上使人愁。
# import os
# file = "poetry.txt"
# f = open(file, "r+", encoding="utf-8")
# new_file = "tmp"
# f_new = open(new_file, "w", encoding="utf-8")
# count = 0
# for count in range(0, 4):
#     new_line = f.readline()
#     count += 1
#     if count == 3:
#         continue
#     else:
#         f_new.write(new_line)
# f.close()
# f_new.close()
# os.replace(new_file, file)



# 20.有名为username.txt的文件，其内容格式如下，写一个程序，判断该文件中是否存在”alex”, 
# 如果没有，则将字符串”alex”添加到该文件末尾，否则提示用户该用户已存在；
# pizza alex egon
# def check_name(user_name):
#     filename = "username.txt"
#     f = open(filename, "r")
#     count = 0
#     for lines in f:
#         new_lines = lines.strip().split()
#         if user_name in new_lines:
#             print("该用户已存在。")
#             count += 1
#             break
#     if count == 0:
#         f = open(filename, "a")
#         f.write(user_name)
#         f.close()
#         print("该用户已添加。")
#     f.close()
# check_name("aaa")
        



# 21.有名为user_info.txt的文件，其内容格式如下，写一个程序，删除id为100003的行； 将id为100002的用户名修改为alex li；
# pizza,100001
# alex, 100002
# egon, 100003
# import os
# def func():
#     filename = "user_info.txt"
#     tmp_file = "tmp_file"
#     f = open(filename, "r+")
#     f_new = open(tmp_file, "w")
#     for lines in f:
#         if '100003' in lines:
#             continue
#         f_new.write(lines)
#     f.close()
#     f_new.close()
#     os.replace(tmp_file, filename)
#     f = open(filename, "r+")
#     f_new = open(tmp_file, "w")
#     for new_lines in f:
#         if '100002' in new_lines:
#             new_lines = new_lines.replace('alex', 'alex li')
#         f_new.write(new_lines)
#     f.close()
#     f_new.close()
#     os.replace(tmp_file, filename)
# func()

# 22.写一个计算每个程序执行时间的装饰器；



# 23.lambda是什么？请说说你曾在什么场景下使用lambda？
# 匿名函数，可以在map() filter()函数下使用



# 24.写一个摇骰子游戏，要求用户压大小，赔率一赔一。要求：三个骰子，每个骰子的值从1-6，摇大小，每次打印摇出来3个骰子的值。