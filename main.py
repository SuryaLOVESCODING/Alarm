import datetime
import time
import sys
from playsound import playsound

current_time = datetime.datetime.now()
 
 
current_year=current_time.year

current_month=current_time.month
 
current_day=current_time.day
 
current_hour=current_time.hour


current_minute=current_time.minute



day_set=str(current_month)+"-"+str(current_day)+"-"+str(current_year)
alarm_set=str(current_hour)+":"+str(current_minute)

print("Set an Alarm (should be in format, 8:30 or 20:30)")
alarm=input("")


print("Set the day (should be in format, 8-9-2023)")
day=input("")


minutes=0

while(True):

    if(alarm==alarm_set and day==day_set):
  
      print(alarm_set)

      while True:
        for i in range(30):
          playsound('C:\\Users\\surya\\Downloads\\audio_alarm.mp3')
      
        question=input("Capital of India:")
        if(question=="New Delhi"):
          print("Good Morning!")
          break
          sys.exit()

      
    





    time.sleep(60)
    current_minute+=1
    minutes+=1
    alarm_set=str(current_hour)+":"+str(current_minute)

      
    if(minutes==60):
      current_hour+=1
      alarm_set=str(current_hour)+":"+str(current_minute)

  
    if(minutes==1440):
      current_year+=1
      day_set=str(current_month)+"-"+str(current_day)+"-"+str(current_year)