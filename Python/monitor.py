#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --- test_embed.py ---
# Author  : samuel.bucquet@gmail.com
# License : GPLv2
"""
"""

#from tkinter import Text, Tk, Frame
from tkinter import*
import sys
import os
import tkinter.scrolledtext as tkst

global autoscroll
autoscroll = False

def tail(f):
	line = f.readline()
	if line :
		logfile.insert('end', line)
		logfile.see(END)
			
	logfile.after(100, tail, f)
	
def tail1(f):
	line = f.readline()
	if line :
		logfile.insert('end', line)
			
	logfile.after(100, tail, f)
	


def callback():
	not(autoscroll)


root = Tk()
logfile = tkst.ScrolledText(root, relief='ridge', bd=2)
b = Button(root, text = "autoscroll", command = callback )
b.pack(side=BOTTOM)
b.config(state = ACTIVE)

logfile.pack()
termf = Frame(root, height=200, width=500, relief='ridge', bd=2)
termf.pack(side=BOTTOM)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 500x200 -e python3 -i -c "import %s" &' % (wid, sys.argv[1]))

if autoscroll == True:
	tail(open(sys.argv[2]))
else :
	tail1(open(sys.argv[2]))

root.mainloop()
