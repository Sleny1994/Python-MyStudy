# -*- coding:utf-8 -*-
import sys

def print_lol(lists, indent = False, level = 0, fn = sys.stdout):
    for each_list in lists:
        if isinstance(each_list, list):
            print_lol(each_list, indent, level+1, fn)
        else:
            if indent:
                for tab in range(level):
                    print("\t", end='', file = fn)
            print(each_list, file = fn)
