#!/usr/bin/python

# logTemp.py
# Heidi Fritz

import sqlite3
import os
import time
""" Log Current Time, Temperature in Celsius and Fahrenheit
   Puts date, time, temperature in a sqlite3 database(testTemp.db) """
def logTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006972625/w1_slave")
	tempfile_text = tempfile.read()
	#currentTime=time.strftime('%x %X %Z')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0

        # Create xdate and xtime strings in Year-Month-Day and Hour-Min-Sec format
        localtime = time.localtime()
        xtime = time.strftime("%H-%M-%S", localtime)
        xdate = time.strftime("%Y-%m-%d", localtime)
   
		# connect to testTemp database
        conn = sqlite3.connect('/home/pi/Documents/EmbeddedLinux/ELSpring2016/code/myTempTime.db')
        print "Opened database successfully."

        # check if the table 'Temperature' already exists
        cursor = conn.cursor()   
        query = cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = 'Temperature';")
        exists = cursor.fetchone()[0]  # fetches result of query
        if not(exists):
           # there are no tables named 'Temperature'
           conn.execute("CREATE TABLE Temperature(DATE TEXT, TIME TEXT, TEMPC INTEGER, TEMPF INTEGER);")
           print "Table created."
           conn.execute("INSERT INTO Temperature(DATE,TIME,TEMPC,TEMPF) VALUES (?, ?, ?, ?);", (xdate, xtime, tempC, tempF))
           conn.commit()
           print "Temp recorded."
        else:
           # there is a table named 'Temperature'
           conn.execute("INSERT INTO Temperature(DATE,TIME,TEMPC,TEMPF) VALUES (?, ?, ?, ?);", (xdate, xtime, tempC, tempF))
           conn.commit()
           print "Temp recorded."
              
        conn.close()

        return 0
    
	
logTemp()
