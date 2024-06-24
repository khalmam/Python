from datetime import datetime
from playsound import playsound
4

#input the time in HH:MM where HH is  hour and MM is minutes in 12 hour format



alarm_date = input('Enter the date in which you want to set the alarm:').strip()
alarm_time = ''.join(input("Enter the time of alarm to be set in HH:MM,AM/PM format:")).split()
alarm_tone = input('Enter m for a music or b for beep sound:')

if alarm_tone == 'b':
   dur = int(input("duration in seconds: "))*1000 #winsound takes in millisecond
   freq = int(input("frequency of the noise:"))#optimal -500

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_period = alarm_time[6:8]


print('setting alarm')

while True:
   current_time =datetime.now()
   current_hour = current_time.strftime('%I')
   current_minute = current_time.strftime('%M')
   current_period = current_time.strftime('%p')
   current_date = current_time.strftime('%d')
   if current_date==alarm_date and current_period==alarm_period and current_hour==alarm_hour and current_minute==alarm_minute:
    print('*'*10)
    print('| '+' wake up! '+' |')
    print('*'*10)
    if alarm_tone =='m':
      playsound('alarm.wav')
    break 