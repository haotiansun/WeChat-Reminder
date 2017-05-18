#!/usr/bin/python
#_*_ coding:utf8 _*_

import itchat
from is_valid_date import is_valid
from threading import Timer
#from datetime import *
#from datetime import datetime
import datetime
import time
from weather_test import show_weather
import weather
import sys

reload(sys)
sys.setdefaultencoding("utf8")

tmp = True  # judge whether the string is a datetime

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print(msg['Text'])

    def send(str1):
        itchat.send(str1, msg['FromUserName'])

    for i in range(len(msg['Text'])):
        if(msg['Text'][i] == '天' and msg['Text'][i + 1] == '气'):
            #str_weather = show_weather()
            str_weather = weather.show_weather()
            send(str_weather)
            break
        if(msg['Text'][i] == '@'):
            for j in range(len(msg['Text'])):
                #allow the input of month with single number
                if msg['Text'][j] == '月':
                    if (j - 2) == -1:
                        str_month = '0' + msg['Text'][j - 1]
                    else:
                        str_month = msg['Text'][j - 2] + msg['Text'][j - 1]

                #allow the input of day with single number
                if msg['Text'][j] == '日':
                    if msg['Text'][j - 2] == '月':
                        str_day = '0' + msg['Text'][j - 1]
                    else:
                        str_day = msg['Text'][j - 2] + msg['Text'][j - 1]

                # allow the input of 'today'
                if msg['Text'][j] == '今' and msg['Text'][j + 1] == '天':
                    datetime_now = datetime.datetime.now()
                    str_month = str(datetime_now.month)
                    str_day = str(datetime_now.day)

                # allow the input of 'tomorrow'
                if msg['Text'][j] == '明' and msg['Text'][j + 1] == '天':
                    today = datetime.date.today()
                    tomorrow = today + datetime.timedelta(days = 1)
                    str_month = str(tomorrow.month)
                    str_day = str(tomorrow.day)

                # allow the input of 'the day after tomorrow'
                if msg['Text'][j] == '后' and msg['Text'][j + 1] == '天':
                    today = datetime.date.today()
                    tomorrow = today + datetime.timedelta(days=2)
                    str_month = str(tomorrow.month)
                    str_day = str(tomorrow.day)

                # allow the input of '2 days after tomorrow'
                if msg['Text'][j] == '大' and msg['Text'][j + 1] == '后' and msg['Text'][j + 2] == '天':
                    today = datetime.date.today()
                    tomorrow = today + datetime.timedelta(days=3)
                    str_month = str(tomorrow.month)
                    str_day = str(tomorrow.day)

                #allow the input of hour with single number
                if msg['Text'][j] == ':' or msg['Text'][j] == '点':
                #    if msg['Text'][j - 2] == '日':
                    if not msg['Text'][j - 2].isdigit():
                        str_hour = '0' + msg['Text'][j - 1]
                    else:
                        str_hour = msg['Text'][j - 2] + msg['Text'][j - 1]
                    if msg['Text'][j + 1] == '@':
                        str_minute = '00'
                    else:
                        str_minute = msg['Text'][j + 1] + msg['Text'][j + 2]


            str_date = '2017-'+ str_month + '-' + str_day + ' ' + str_hour + ':'+ str_minute + ':00'
            str_date1 = str_date
            is_valid(str_date, tmp)
            print(tmp)
            if tmp == True:
                send('已收到')
                datetime_dest = datetime.datetime.strptime(str_date1, '%Y-%m-%d %H:%M:%S')
                #get the timestamp of now and the prospective time
                timestamp_dest = time.mktime(datetime_dest.timetuple())
                datetime_now = datetime.datetime.now()
                timestamp_now = time.mktime(datetime_now.timetuple())
                #get the length of time
                timestamp_delta = timestamp_dest - timestamp_now
                #use Timer to send the message later
                Timer(timestamp_delta, send, (msg['Text'],)).start()
            else:
                send('输入有误')
            break


print('start')
itchat.auto_login(hotReload=True)
print(itchat.get_friends(True))
itchat.run()
