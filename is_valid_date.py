#!/usr/bin/python
#_*_ coding:utf8 _*_

import sys
import time
reload(sys)

sys.setdefaultencoding("utf8")

def is_valid(str, a):
 '''判断是否是一个有效的日期字符串'''
a = True
try:
    time.strptime(str, "%Y-%m-%d %H:%M:%S")
    a = True
except:
    a = False
