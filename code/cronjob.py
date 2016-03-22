#!/usr/bin/python

# cronjob.py
# Heidi Fritz


from crontab import CronTab  # must do 'sudo pip install python-crontab'

def createJob():
        cron = CronTab(user='root')
        job = cron.new(command='sudo python /home/pi/Documents/EmbeddedLinux/ELSpring2016/code/logTemp.py')
        job.minute.every(1)
        job.enable()
        cron.write()
        if cron.render():
            print cron.render()
        print "CronJob created."
        return 0


createJob()
