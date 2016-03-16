#!/usr/bin/python

# logTime.py
# Heidi Fritz
# Log the date and time to a sqlite database. Create a testTime.db 
# database file with two text columns to hold these values.
# Every time you call the python function logTime(), the 
# current date and time should be logged to the db file.

import time
import sqlite3

def logTime():
   # Create xdate and xtime strings in Year-Month-Day and Hour-Min-Sec format
   localtime = time.localtime()
   xtime = time.strftime("%H-%M-%S", localtime)
   xdate = time.strftime("%Y-%m-%d", localtime)
   
   # connect to testTime database
   conn = sqlite3.connect('testTime.db')
   print "Opened database successfully."

   # check if the table 'TIME' already exists
   cursor = conn.cursor()   
   query = cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = 'TIME'")
   exists = cursor.fetchone()[0]  # fetches result of query
   if exists:
      # there is a table named 'TIME'
      conn.execute("INSERT INTO TIME(DATE,TIME) VALUES (?, ?);", (xdate, xtime))
      conn.commit()
      print "Time recorded."
   else:
      # there are no tables named 'TIME'
      conn.execute("CREATE TABLE TIME (DATE TEXT, TIME TEXT);")
      print "Table created."
      conn.execute("INSERT INTO TIME(DATE,TIME) VALUES (?, ?);", (xdate, xtime))
      conn.commit()
      print "Time recorded."
      
   conn.close()

   return 0
   
logTime()
