# -*- coding:UTF-8 -*-
filename = "stock_data.txt"
flag = True
count = 0

while flag:
    enter = input("股票查询接口>>：")

    if enter.find(">") != -1:
        new1_enter = enter.split(">")
        f = open(filename, "r", encoding="utf-8")
        for lines in f:
            lines_str = lines.strip()
            lines_list = lines_str.split()
            if lines_list[0].isdigit() == False:
                continue
            if new1_enter[0] == "最新价":
                if float(lines_list[3]) > float(new1_enter[1]):
                    count += 1
                    print(lines_list)
            elif new1_enter[0] == "涨跌幅":
                if float(lines_list[4].split("%")[0]) > float(new1_enter[1]):
                    count += 1
                    print(lines_list)
            elif new1_enter[0] == "换手率":
                if float(lines_list[-3].split("%")[0]) > float(new1_enter[1]):
                    count += 1
                    print(lines_list)
        print("找到%s条" % count)
        count = 0
        f.close()

    elif enter.find("<") != -1:
        new2_enter = enter.split("<")
        f = open(filename, "r", encoding="utf-8")
        for lines in f:
            lines_str = lines.strip()
            lines_list = lines_str.split()
            if lines_list[0].isdigit() == False:
                continue
            if new2_enter[0] == "最新价":
                if float(lines_list[3]) < float(new2_enter[1]):
                    count += 1
                    print(lines_list)
            elif new2_enter[0] == "涨跌幅":
                if float(lines_list[4].split("%")[0]) < float(new2_enter[1]):
                    count += 1
                    print(lines_list)
            elif new2_enter[0] == "换手率":
                if float(lines_list[-3].split("%")[0]) < float(new2_enter[1]):
                    count += 1
                    print(lines_list)
        print("找到%s条" % count)
        count = 0
        f.close()

    elif enter == "exit":
        exit()

    else:
        f = open(filename, "r", encoding="UTF-8")
        for lines in f:
            lines_str = lines.strip()
            lines_list = lines_str.split()
            if enter in lines_list[2]:
                count += 1
                print(lines_list)
                continue
        print("找到%s条" % count)
        count = 0
        f.close()
