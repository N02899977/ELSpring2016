#!/usr/bin/python
#
# Script for AndyPi 16x2 HD44780 LCD
# Developed by: AndyPi (http://andypi.co.uk/)
# Date   : 26/03/2013
# Version 1.1
#
# lcd.lcd_init(); required to initialised LCD
# lcd.led(value); turn on backlight, value = 0:512
# lcd.static_text(line, "justification", "Static Message")
# lcd.cls(); clears LCD & turns off backlight    
#
# Note: clock, scroll_clock, scroll are all infinite loop functions.
# Therefore, you can't add any further python commands after these
# unless you run them inside a seperate thread process
# as shown in this example
#
# lcd.clock(line, "justification"); line = 1,2; justification =l,r,c
# lcd.scroll_clock(line, "justification", speed, "Scrolling Message"); line & justification refer to clock;  speed = 0:1s
# lcd.scroll(line, speed, "Scrolling Message");
	
# import required functions
from AndyPi_LCD import AndyPi_LCD
from processing import Process
import time
import feedparser
	
if __name__ == '__main__':
	# initial check for latest rss feed
	msg=feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk').entries[0].title
	lcd=AndyPi_LCD()  # set name of imported class
	lcd.lcd_init()    # initialise LCD
	lcd.led(512)      # turn backlight fully on
	
	while True:
		# setup a new thread process, in which to run the lcd.scroll_clock function, with the correct arguments
		p = Process(target=lcd.scroll_clock, args=(1, "c", 0.3, msg))
		# start the process
		p.start()
		# wait for 30 seconds (or however long you wish to wait between checking updates)
		time.sleep(30.0)
		# while the python is scrolling the LCD message in the 'p' process
		# check for new rss feed, and put in variable "msg"
		msg=feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml?edition=uk').entries[0].title
		# stop the scroller process
		p.terminate()

