#!/usr/bin/python

## This script, when executed, sends an email message from your Pi 
## to a specified recipient with a brief message.

## First you must set up 2-step verication with google accounts. Then get an App-specific password  
## that you can use with your Pi. This password is used in the script below.
## See https://support.google.com/accounts/answer/185833?hl=en

import smtplib
import mimetypes
import email
import email.mime.application
import sys
from time import strftime
from email.MIMEBase import MIMEBase
from email import Encoders

me='fritz.heidi@gmail.com'  #####Sender's email####
you='fritzh1@hawkmail.newpaltz.edu'     ### Receiver's email########
another='anotherPerson@gmail.com'   ### Another recipient ####
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'From Pi'
msg['From'] = me
msg['To'] = you
body=email.mime.Text.MIMEText("This is from Heidi's Pi"+strftime("%Y-%m-%d %H:%M:%S"))

part = MIMEBase('application',"octet-stream")
part.set_payload(open("LED_blink50.py", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="LED_blink50.py"')

msg.attach(part)
msg.attach(body)
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(me,'tqbh aliz vhvm ppeu') ## Use your App-specific password from google##########
s.sendmail(me,[you],msg.as_string())
s.quit()

##References
###https://docs.python.org/2/library/email-examples.html
###http://solvingmytechworld.blogspot.com/2013/01/send-email-through-gmail-running-script.html
### http://stackoverflow.com/questions/1966073/how-do-i-send-attachments-using-smtp/8243031#8243031
