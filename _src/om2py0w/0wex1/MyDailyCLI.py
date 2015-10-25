#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys,time

def print_last_f():
    with open("name_file.txt", "a+") as name_fp:
        for f_name in name_fp:
            print "----------------------------------->\nDate: " + f_name[:-5] + "\n"
            with open(f_name[:-1], "r") as fp:
                for content in fp:
                    print content
            print "<-----------------------------------\n"

def update_name_f(new_f):
    i = 0
    with open("name_file.txt", "a+") as name_fp:
        for f_name in name_fp:
            if new_f == f_name[:-1]:
                i = 1
        if i == 0 and new_f != "":
            new_f += '\n'
            name_fp.write(new_f)

def entrance():
    print "History content:\n"
    print_last_f()
    print "Begin writing!\n"
    print "You can type q or Q to quit!\n"
    f_name = time.strftime('%Y-%m-%d', time.localtime(time.time())) + ".txt"
    update_name_f(f_name)
    fp = open(f_name, 'a+')
    rd_line = ""
    while True:
        rd_line = raw_input() + '\n'
        if rd_line == "q\n" or rd_line == "Q\n":
            break
        fp.write(rd_line)
    fp.close()
    print "You have been exited."

if __name__ == '__main__':
    entrance