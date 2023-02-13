import os
import datetime
import time

day, month, year = input("Enter the Time = ").split("/")
hour, minute, second = input("Enter the time = ").split(":")
shedule_date = datetime.date(int(year), int(month), int(day))
n = 1
while n>0:
    if time.localtime().tm_hour == int(hour) and time.localtime().tm_min == int(minute) and time.localtime().tm_sec == int(second):
        os.startfile("D:\\Movies\\Beautiful bangladesh\\Ke-Tumi-Je-(Romantic)(MrSong.In).mp3")
        break
    else: 
        print(time.localtime().tm_sec)
        n = n + 1
