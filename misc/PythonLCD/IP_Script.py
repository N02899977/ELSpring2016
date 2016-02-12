#!/usr/bin/python
#
# IP address script for AndyPi 16x2 HD44780 LCD
# Developed by: AndyPi (http://andypi.co.uk/)
# Date   : 19/10/2013
# Version 1.1
#
# lcd.lcd_init(); required to initialised LCD
# lcd.led(value); turn on backlight 0:512
# lcd.static_text(line, "justification", "Static Message")
# lcd.cls(); clears LCD & turns off backlight

from subprocess import *
from AndyPi_LCD import AndyPi_LCD

def run_cmd(cmd):
        # runs whatever is in the cmd variable in the terminal
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1" # get ip address of eth0 connection (use wlan0 for wireless)
ipaddr = run_cmd(cmd)[:-1] # set output of command into ipaddr variable

lcd=AndyPi_LCD()  # set name of class
lcd.lcd_init()    # initialise
lcd.led(512)      # turn backlight fully on
lcd.static_text(2,"c",ipaddr)   # center static text IP address on line 2
lcd.static_text(1,"c", "My IP address:")

