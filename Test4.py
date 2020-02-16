# -*- coding:UTF-8 -*-

import sys
import os

old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]
filename_new = "tmp_txt"

f = open(filename, "r")
f_new = open(filename_new, "w")

count = 0

for line in f:
    if old_str in line:
        line = line.replace(old_str, new_str)
        count += line.count(new_str)
    f_new.write(line)

os.replace(filename_new, filename)

print("总计替换了 %s" % count + " 处内容。")
