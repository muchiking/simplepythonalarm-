import datetime
import time

from playsound import playsound
#timer
## this is a simple app that acts as a timer

def checker(timein_hours,timeinmins):
    time2=[]
    time2.append(datetime.datetime.now())
    #time_now=datetime.datetime.now()
    new_time = time2[0] + datetime.timedelta(hours=timein_hours, minutes=timeinmins)
    print(new_time)
    while new_time >= time2[0]:
        time.sleep(30)
        time2.append(datetime.datetime.now())
        print(time2)
        del time2[0]
    else:
        playsound('alarm.mp3')


timein_hours =int(input("enter time in hours"))
timeinmins = int(input("enter time in minutes"))
checker(timein_hours,timeinmins)