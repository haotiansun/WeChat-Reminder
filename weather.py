#!/usr/bin/python
#_*_ coding:utf8 _*_

#import urllib.request
import urllib2
import urllib
import urlparse
#import urllib.parse
import json
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
"""
 利用“最美天气”抓取即时天气情况
 http://www.zuimeitianqi.com/

"""


class ZuiMei():
    def __init__(self):
        self.url = 'http://www.zuimeitianqi.com/zuimei/queryWeather'
        self.headers = {}
        self.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        # 部分城市的id信息
        self.cities = {}
        self.cities['成都'] = '01012703'
        self.cities['杭州'] = '01013401'
        self.cities['深圳'] = '01010715'
        self.cities['广州'] = '01010704'
        self.cities['上海'] = '01012601'
        self.cities['北京'] = '01010101'
        # Form Data
        self.data = {}
        self.city = '北京'

    def query(self, city='北京'):
        if city not in self.cities:
            print('暂时不支持当前城市')
            return
        self.city = city
        data = urllib.urlencode({'cityCode': self.cities[self.city]}).encode('utf-8')
        #req = urllib.request.Request(self.url, data, self.headers)
        req = urllib2.Request(self.url, data, self.headers)
        response = urllib2.urlopen(req)

        html = response.read().decode('utf-8')
        # 解析json数据并打印结果
        str = self.json_parse(html)
        return str
        #return self.json_parse(html)

    def json_parse(self, html):
        target = json.loads(html)
        high_temp = target['data'][0]['actual']['high']
        low_temp = target['data'][0]['actual']['low']
        current_temp = target['data'][0]['actual']['tmp']
        today_wea = target['data'][0]['actual']['wea']
        weas = today_wea.split("/")
        def getweather(num):
            wea = "a"
            if num == 0:
                wea = "晴"
            elif num == 1:
                wea = "多云"
            elif (num == 2):
                wea = "阴";
            elif (num == 3) :
                wea = "阵雨";
            elif (num == 4) :
                wea = "雷阵雨";
            elif (num == 5) :
                wea = "雷阵雨并伴有冰雹";
            elif (num == 6) :
                wea = "雨夹雪";
            elif (num == 7) :
                wea = "小雨";
            elif (num == 8) :
                wea = "中雨";
            elif (num == 9) :
                wea = "大雨";
            elif (num == 10) :
                wea = "暴雨";
            elif (num == 11) :
                wea = "大暴雨"
            elif (num == 12) :
                wea = "特大暴雨";
            elif (num == 13):
                wea = "阵雪";
            elif (num == 14) :
                wea = "小雪";
            elif (num == 15) :
                wea = "中雪";
            elif (num == 16) :
                wea = "大雪";
            elif (num == 17) :
                wea = "暴雪";
            elif (num == 18) :
                wea = "雾";
            elif (num == 19) :
                wea = "冻雨";
            elif (num == 20) :
                wea = "沙尘暴";
            elif (num == 21) :
                wea = "小雨-中雨";
            elif (num == 22) :
                wea = "中雨-大雨";
            elif (num == 23) :
                wea = "大雨-暴雨";
            elif (num == 24) :
                wea = "暴雨-大暴雨";
            elif (num == 25) :
                wea = "大暴雨-特大暴雨";
            elif (num == 26) :
                wea = "小雪-中雪";
            elif (num == 27) :
                wea = "中雪-大雪";
            elif (num == 28) :
                wea = "大雪-暴雪";
            elif (num == 29) :
                wea = "浮沉";
            elif (num == 30) :
                wea = "扬沙";
            elif (num == 31) :
                wea = "强沙尘暴";
            elif (num == 32) :
                wea = "飑"
            elif (num == 33) :
                wea = "龙卷风"
            elif (num == 34) :
                wea = "若高吹雪"
            elif (num == 35) :
                wea = "轻雾"
            elif (num == 53) :
                wea = "霾"
            elif (num == 99):
                wea = "未知"
            return wea

        #print len(weas)
        #print weas[0]
        #print(getweather(0))
        #print type(weas[0])
        if len(weas) == 1:
            name = getweather(int(weas[0]))

        elif len(weas) == 2:
            name = getweather(int(weas[0])) + "转" + getweather(int(weas[1]))
        else:
            weas[0] == 99

        print name
        #print name
        air_desc = target['data'][0]['actual']['desc']
        wind = target['data'][0]['actual']['ws']
        air = target['data'][0]['air']
        pubTimes = target['data'][0]['actual']['PTm'].split(" ");
        pubTime = pubTimes[1]
        pubTime = "今天" + pubTime + "发布";
        print air['aqigrad']
        print air['pm2'] + air['pm10']
        print pubTime
        # 上海 6~-2°C 现在温度 1°C 湿度：53 空气质量不好，注意防霾。
        return str(str(datetime.date.today()) + '\n' + self.city + ' ' + str(high_temp) + '~-' + str(low_temp) + '℃\n' + '现在温度： ' + str(current_temp) + '°C 湿度：' + str(today_wea) + '\n' + str(air_desc)) + str(wind)


def show_weather():
    zuimei = ZuiMei()
    str = zuimei.query('北京')
    return str
print(show_weather())