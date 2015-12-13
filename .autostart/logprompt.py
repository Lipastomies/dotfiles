#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  logprompt.py
#
#A really simple prompt for starting the wm/de of my choice.
#Used in conjunction with a small bash script that starts the wm
#
#Author: Arto Lehisto

import curses, sys

#init curses
def main():
    retval = 1
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
        #the index
    i3 = "1) i3 (X11)"
    sway = "2) Sway (Wayland)"
    tty = "3) none (just tty)"
    clr = "                                                                  "
    idx = 1
    key = '0'
    cnt = 0
    choice = 0
    ch = 0
    while cnt < 10 :
        op = 0
        #a = threading.Thread(target = input_thread,args = (kpr,stdscr))
        stdscr.addstr(2,0,clr)
        if cnt % 2 == 0:
            op = curses.A_REVERSE
        stdscr.addstr(0,0,"Starting system... Autostarting option 1 in {} s".format((11-cnt)//2),op)
        #stdscr.addstr(1,0,"Choose your window manager:",op)
        #stdscr.addstr(2,0,i3, op)
        #stdscr.addstr(2,20,sway, op)
        #stdscr.addstr(2,40,tty, op)
        stdscr.refresh()
        #a.start()
        try:
            curses.halfdelay(5)
            tmp = stdscr.getkey()
        except:
            cnt +=1
        else:
            choice = 1
            key = tmp
            break
    #curses.nocbreak()
    stdscr.clear()
    curses.cbreak()
    if choice:
        while key != 'q' and key != '\n':
            option = [0,0,0]
            option[idx-1] = curses.A_REVERSE
            stdscr.addstr(2,0,clr)
            stdscr.addstr(0,0,"Starting WM/DE")
            stdscr.addstr(1,0,"Choose:")
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
    else:
        retval = 1
    #exit curses
    curses.nocbreak()
    curses.echo()
    stdscr.keypad(False)
    curses.endwin()
    return retval
    
retval = main()
sys.exit(retval)
