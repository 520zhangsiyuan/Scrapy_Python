# -*- coding: utf-8 -*-
import scrapy
from icauto.items import IcautoItem
import time

class IcautosSpider(scrapy.Spider):
    name = 'icautos'
    allowed_domains = ['icauto.com.cn']
    url = "https://www.icauto.com.cn/cdz/"
    sumer = 14323
    start_urls = [url+str(sumer)+'.html']
#    download_delay = 20
    def parse(self, response):
        self.sumer +=  1
        new_url = self.url+str(self.sumer)+'.html'
        item = IcautoItem()
	#简介
        cdz = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='cdz-ty cdz-address'])").extract()[0]
        #地址
        adress = response.xpath("normalize-space(//div[@class='tdz-ty-left']/div[@class='cdz-ty cdz-address'])").extract()[0]
        #名称
        name = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='cdz-ty cdz-name'])").extract()[0]
        #支付方式
        pay = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='tdz-ty-left']/div[@class='cdz-ty cdz-pay'])").extract()[0]
        #充电费
        chargefee = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='tdz-ty-left']/div[@class='cdz-ty cdz-powfee'])").extract()[0]
        #服务费
        servicefee = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='tdz-ty-left']/div[@class='cdz-ty cdz-servicefee'])").extract()[0]
        #停车费
        parkingfee = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='tdz-ty-left']/div[@class='cdz-ty cdz-parkfee'])").extract()[0]
        #开放时间
        date = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='tdz-ty-left']/div[@class='cdz-ty cdz-opentime'])").extract()[0]
        #充电桩个数
        num = response.xpath("normalize-space(//div[@class='cdz-r']/div[@class='tdz-ty-left']/div[@class='cdz-num'])").extract()[0]
#        if adress.strip()=='':
#                yield scrapy.Request(new_url, callback = self.parse)
#        else:
#                if self.sumer < 18171:
        item['name'] = name.encode('utf-8')
        item['adress'] = adress.encode('utf-8')
        item['pay'] = pay.encode('utf-8')
        item['chargefee'] = chargefee.encode('utf-8')
        item['servicefee'] = servicefee.encode('utf-8')
        item['parkingfee'] = parkingfee.encode('utf-8')
        item['date'] = date.encode('utf-8')
        item['num'] = num.encode('utf-8')
	item['cdz'] = cdz.encode('utf-8')
#	time.sleep(10)
        yield scrapy.Request(new_url, callback = self.parse)
        yield item

