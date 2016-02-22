# myBlinkingLed.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def blink(pin):
   try:
      # blink 3 times rapidly, then off 5 seconds 
      for i in range(0,3):
	print "blink #" + str(i+1)
	GPIO.output(pin,True)
	time.sleep(.08)
	GPIO.output(pin,False)
	if i == 2:
	   time.sleep(5)
	else:
	   time.sleep(.08)
      print "done"

      # blink 4 times rapidly, then 5 second pause
      for i in range(0,4):
	print "blink #" + str(i+1)
	GPIO.output(pin,True)
	time.sleep(.08)
	GPIO.output(pin,False)
	if i == 3:
   	   time.sleep(5)
	else:
	   time.sleep(.08)
      print "done"

   except KeyboardInterrupt:
      print "Keyboard Interrupt."
      
while (1): 
   blink(17)
   GPIO.cleanup()