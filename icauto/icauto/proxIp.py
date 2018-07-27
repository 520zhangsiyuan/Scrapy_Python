# -*- coding: UTF-8 -*-
import requests;
import time;
import threading;
from settings import IPPOOL;
from requests.packages import urllib3;
import os
ips = [];

# 获取代理IP的线程类
class GetIpThread(threading.Thread):
    def __init__(self,fetchSecond):
        super(GetIpThread, self).__init__();
        self.fetchSecond=fetchSecond;
    def run(self):
        global ips;
        while True:
            # 获取IP列表
            res = requests.get(apiUrl).content.decode()
            # 按照\n分割获取到的IP
            IPPOOL = res.split('\n');
	    print IPPOOL
            # 休眠
            time.sleep(self.fetchSecond);		
class startThread(threading.Thread):
    def __init__(self,startscrapy):
        super(startThread, self).__init__();
        self.startscrapy=startscrapy;
    def run(self):
	os.system(self.startscrapy)
if __name__ == '__main__':
    # 这里填写无忧代理IP提供的API订单号（请到用户中心获取）
    order = "8df8d026cfe979c1d4a3e2cde279e2a2";
    # 获取IP的API接口
    apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order;
    # 获取IP时间间隔，建议为5秒
    fetchSecond = 5;
    # 开始自动获取IP
    GetIpThread(fetchSecond).start();
    startscrapy = 'scrapy crawl icautos'   
    startThread(startscrapy).start()
