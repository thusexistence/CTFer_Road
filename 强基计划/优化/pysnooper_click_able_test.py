# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/12/4 0004 17:01
"""
举个例子，统计requests.get运行轨迹，requests和urllib发http请求各执行了多少行代码。

requests请求http百度，会花费18635行代码，requests如果请求https需要执行达到4万多行，性能更是严重下降
urllib 请求百度http ，会花费11902行代码

普通3Ghz以下的电脑，单进程运行python，选一个或者自己做一个流量消耗非常少的http接口进行请求测试，
平均每秒不可能运行超过300次请求。
所以大规模发requests不是简单的io密集型，也是消耗性能的，
包括最牛的英特尔5Ghz的频率，单核如果每秒能运行1000次requests请求，我愿意把电脑cpu吃了。
"""

import requests
import urllib3
from urllib import request
from pysnooper_click_able import snoop
#
# ss = requests.session()
@snoop(depth=100,dont_effect_on_linux=False)
def f():
   # requests.get('http://www.baidu.com')
   # requests.get('http://www.sina.com')
   response = request.urlopen('http://www.baidu.com')
   # ss.get('http://www.baidu.com')


f()