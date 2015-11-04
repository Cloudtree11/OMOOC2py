#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys,time

# 打印之前的日记内容
def print_last_f(str_content):
    temp_str = ''
    # name_file.txt 保存之前的每一个文件名
    with open("diary_history/name_file.txt", "r") as name_fp:
        # 读取每一个记录文件的文件名
        for f_name in name_fp:
            temp_str = "----------------------------------->\nDate: " + f_name[:-5] + "\n"
            # 打印保存的每一个文件中的内容
            with open("diary_history/" + f_name[:-1], "r") as fp:
                for content in fp:
                    temp_str += content
            temp_str += "<-----------------------------------\n"
            str_content = temp_str

# 更新 name_file.txt 中的文件名
def update_name_f(new_f):
    temp_str = ""
    temp_str = new_f
    i = 0
    with open("diary_history/name_file.txt", "a+") as name_fp:
        for f_name in name_fp:
            if temp_str == f_name[:-1]:
                # i 用来标记文件名是否已有（是否需要记录新的文件名）
                i = 1
        if i == 0 and temp_str != "":
            temp_str += '\n'
            name_fp.write(temp_str)

def entrance(str_content):
    #print "History Diary Content:\n"
    # 先打印之前的日记内容
    #print_last_f()
    #print "Begin writing!\n"
    #print "You can type \':q\' or \':Q\' to exit.\n"
    # 获取当前的日期，作为保存的文件名
    temp_str = ""
    temp_str = str_content
    f_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".txt"
    # 更新文件名列表
    update_name_f(f_name)
    f_name = "diary_history/" + f_name
    fp = open(f_name, 'a+')
    temp_str += '\n'
    fp.write(temp_str)
    fp.close()
    print "You have been exited."

if __name__ == '__main__':
    entrance()