#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --- test_embed.py ---
# Author  : samuel.bucquet@gmail.com
# License : GPLv2
"""
"""


from tkinter import Text, Tk, Frame, Scrollbar
import sys
import os

"""
global autoscroll
autoscroll = False
"""
def tail(f):
    line = f.readline()
    while line:
        logfile.insert('end', line)
        logfile.see("end")
        line = f.readline()
    logfile.after(100, tail, f)


root = Tk()
""""
def callback():
	not(autoscroll)
"""
logframe = Frame(root, relief='ridge', bd=2)
logframe.grid_rowconfigure(0, weight=1)
logframe.grid_columnconfigure(0, weight=1)
sb = Scrollbar(logframe)
sb.grid(row=0, column=1, sticky='n s')
logfile = Text(logframe, wrap='word', yscrollcommand=sb.set)
logfile.grid(row=0, column=0, sticky='n s e w')
sb.config(command=logfile.yview)
logframe.pack()
"""b = Button(root, text = "autoscroll", command = callback )
b.pack(side=BOTTOM)
b.config(state = ACTIVE)
"""
termf = Frame(root, height=200, width=500, relief='ridge', bd=2)
termf.pack()
wid = termf.winfo_id()
os.system('urxvt -embed {} -geometry 500x200 -e python3 -i -c "from {} import*" &'.format(wid, sys.argv[1]))

tail(open(sys.argv[2]))

