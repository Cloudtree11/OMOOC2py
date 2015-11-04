#!/usr/bin/env python
# -*- coding: utf8 -*-

from Tkinter import *
from MyDailyCLI import *

class MyDailyTk(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createLabel()
        self.createEntry()

    def createEntry(self):
        self.Input = Entry(self)
        self.Input.pack(fill=X)
        self.input_content = StringVar()
        self.Input["textvariable"] = self.input_content
        self.Input.bind('<Key-Return>',
                        entrance(self.input_content))
        
        

    def createLabel(self):
        self.Content = Label(self)
        self.Content.pack(fill=Y, expand=1)
        self.output = StringVar()
        self.Content["textvariable"] = self.output
        print_last_f(self.output)

root = Tk()
#app = Application(master=root)
app = MyDailyTk(master=root)
app.master.title("MyDailyTk")
app.mainloop()
root.destory()