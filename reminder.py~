#!/usr/bin/python
#_*_ coding:utf8 _*_

import itchat
from is_valid_date import is_valid
from threading import Timer
from datetime import datetime
import time
from weather_test import show_weather
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
            str_weather = show_weather()
            send(str_weather)
        if(msg['Text'][i] == '@'):
            for j in range(len(msg['Text'])):
                if msg['Text'][j] == '月':
                    str_month = msg['Text'][j - 2] + msg['Text'][j - 1]
                if msg['Text'][j] == '日':
                    str_day = msg['Text'][j - 2] + msg['Text'][j - 1]
                if msg['Text'][j] == ':':
                    str_hour = msg['Text'][j - 2] + msg['Text'][j - 1]
                    str_minute = msg['Text'][j + 1] + msg['Text'][j + 2]
            str_date = '2017-'+ str_month + '-' + str_day + ' ' + str_hour + ':'+ str_minute + ':00'
            str_date1 = str_date
            is_valid(str_date, tmp)
            print(tmp)
            if tmp == True:
                datetime_dest = datetime.strptime(str_date1, '%Y-%m-%d %H:%M:%S')
                #get the timestamp of now and the prospective time
                timestamp_dest = time.mktime(datetime_dest.timetuple())
                datetime_now = datetime.now()
                timestamp_now = time.mktime(datetime_now.timetuple())
                #get the length of time
                timestamp_delta = timestamp_dest - timestamp_now
                #use Timer to send the message later
                Timer(timestamp_delta, send, (msg['Text'],)).start()
            break

print('start')
itchat.auto_login(hotReload=True)
print(itchat.get_friends(True))
itchat.run()
