# -*- coding:UTF-8 -*-
import os # 导入os模块，用于最后的文件重命名

tips = "模拟登录"
tips = tips.center(20, "-")
filename = "member"
filename_new = "tmp_txt"
print(tips)
count = 0

flag = True # 定义while循环是否执行，True时无限循环，False时则跳出循环
flag2 = 0 # 标记用户名和密码是否正确，默认为0，如若正确则重新赋值为1

while flag:
    user_name = input("请输入您的用户名：")
    user_pass = input("请输入您的密码：")

    f = open(filename, "r+") # 打开文件，用于读取数据
    
    for line_str in f: # 循环遍历文件内容
        line_str = line_str.strip() # 去除文件内字符前后的空格
        line_list = line_str.split() # 按空格切片字符，转成列表
        if user_name == line_list[0] and user_pass == line_list[1] and line_list[2] == "0" : # 判断用户名和密码是否正确，且账号未被锁定
            print("登陆成功！")
            flag = False
            flag2 = 1
            continue
        elif user_name == line_list[0] and line_list[2] == "1": # 判断账号是否锁定
            print("该账号已被禁用，请联系管理员处理！")
            flag = False
    
    if flag2 == 0: # 当用户名或密码错误时，输出
        print("您输入的用户名或密码错误，请重新输入！")
        count += 1
    if count == 3: # 计数三次输错后，锁定账号
        print("您已输入三次错误的用户名或密码，您的账号已被锁定！")
        f = open(filename, "r")
        f2 = open(filename_new, "w")
        for line_str in f: # 将member文件内的内容循环输出，并替换账号锁定标志，0 -> 1
            if user_name in line_str:
                line_str = line_str.replace("0", "1")    
            f2.write(line_str)
        f2.close()
        os.replace(filename_new, filename) # 重命名文件
        break

    f.close()
