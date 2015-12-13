#usr/bin/sh
python ~/.autostart/logprompt.py
x=$?
if [ "$x" = "1" ]; then
    startx
    else
        if [ "$x" = "2" ]; then
            XKB_DEFAULT_LAYOUT=fi sway & 
        fi
fi
clear
