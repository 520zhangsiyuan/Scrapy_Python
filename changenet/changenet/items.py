# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChangenetItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
 	#地址
        adress = scrapy.Field()
        #名称
        name = adress = scrapy.Field()
        #支付方式
        pay = scrapy.Field()
        #充电费
        chargefee = scrapy.Field()
        #服务费
        servicefee = scrapy.Field()
        #停车费
        parkingfee = scrapy.Field()
        #开放时间
        date = scrapy.Field()
        #充电桩个数
        num = scrapy.Field()

