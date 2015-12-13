#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  logprompt.py
#Author: Arto Lehisto
import curses, sys

#init curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
retval = 0
    #the index
i3 = "1) i3 (X11)"
sway = "2) Sway (Wayland)"
tty = "3) none (just tty)"
clr = "                                 "
idx = 1
key = '0'
#the threaded start
kpr = []
cnt = 0
choice = 0
ch = 0
while cnt < 5 :
    #a = threading.Thread(target = input_thread,args = (kpr,stdscr))
    stdscr.addstr(2,0,clr)
    stdscr.addstr(0,0,"Starting system... Autostarting option 1 in {} s".format(5-cnt))
    stdscr.addstr(1,0,"Choose your window manager:")
    stdscr.addstr(2,0,i3, curses.A_BLINK)
    stdscr.addstr(2,20,sway, curses.A_BLINK)
    stdscr.addstr(2,40,tty, curses.A_BLINK)
    stdscr.refresh()
    #a.start()
    try:
        curses.halfdelay(10)
        stdscr.getkey()
    except:
        cnt +=1
    else:
        choice = 1
        break
if choice:
    while key != 'q':
        option = [0,0,0]
        option[idx-1] = curses.A_REVERSE
        stdscr.addstr(2,0,clr)
        stdscr.addstr(0,0,"Starting system...")
        stdscr.addstr(1,0,"Choose your window manager:")
        stdscr.addstr(2,0,i3, option[0])
        stdscr.addstr(2,20,sway, option[1])
        stdscr.addstr(2,40,tty, option[2])
        #stdscr.addstr(3,0,"Idx is {}".format(idx))
        stdscr.refresh()
        key = stdscr.getkey()
        if key == "KEY_LEFT" and idx > 1:
            idx -= 1
        if key == "KEY_RIGHT" and idx < 3:
            idx += 1
        if key == "\n":
            break
retval = idx
#exit curses
curses.nocbreak()
curses.echo()
stdscr.keypad(False)
curses.endwin()
sys.exit(retval)
