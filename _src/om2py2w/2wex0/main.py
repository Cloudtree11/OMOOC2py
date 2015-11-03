#!/usr/bin/env python
# -*- coding: utf8 -*-

from Tkinter import *

class MyDailyTk(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createLabel()
        self.createEntry()

    def createEntry(self):
        self.Input = Entry(self)
        self.Input.pack(fill=X)
        

    def createLabel(self):
        self.Content = Label(self)
        self.Content["text"] = "Date:\nNow\nTest\n"
        self.Content.pack(fill=Y, expand=1)

root = Tk()
#app = Application(master=root)
app = MyDailyTk(master=root)
app.mainloop()
root.destory()