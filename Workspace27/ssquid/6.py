import time

inp_time = input("Enter msec")

sec = int(inp_time/1000.0)
minute = int(sec/60.0)
hour= int(minute/60.0)

minutes = int(minute - hour*60)
second = str(sec - (minutes*60) - (hour*3600))

print str(hour)+":"+str(minutes)+":"+second
