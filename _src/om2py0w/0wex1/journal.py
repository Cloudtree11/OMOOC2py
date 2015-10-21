import sys

def print_last_f():
    name_fp = open("name_file.txt", "a+")
    #f_names = name_fp.readlines()
    for f_name in name_fp:
        print f_name + "------------>\n"
        print f
        fp = open(f_name[:-1], "r")
        for content in fp:
            print content
        fp.close()

def update_name_f(new_f):
    i = 0
    name_fp = open("name_file.txt", "a+")
    #f_names = name_fp.readlines()
    for f_name in name_fp:
        if new_f == name_fp:
            i = 1
    if i == 0 and new_f != "":
        new_f.join('\n')
        name_fp.write(new_f)
    name_fp.close()

def entrance():
    print "History content:\n"
    print_last_f()
    f_name = ""
    f_name = raw_input("Please name your file:")
    update_name_f(f_name)
    print "Begin writing!\n"
    print "You can type q or Q to quit!\n"
    
    fp = open(f_name, 'a+')
    rd_line = "a"
    while True:
        rd_line = raw_input() + '\n'
        if rd_line == "q\n" or rd_line == "Q\n":
            break
        fp.write(rd_line)
    fp.close()
    print "You have been exited."

