# -*- coding: utf-8-*-

import requests
import json

url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100'
jsonStr = requests.get(url).text

data = json.loads(jsonStr)
weather = data["data"]

def show_weather():
    return weather["forecast"][0]["date"] + ' ' + weather["forecast"][0]["type"] + '\n' + weather["forecast"][0]["high"] + ' ' + weather["forecast"][0]["low"] + '\n' + weather["forecast"][0]["fengxiang"] + ' ' + weather["forecast"][0]["fengli"]
