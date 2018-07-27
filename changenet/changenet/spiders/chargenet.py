# -*- coding: utf-8 -*-
import scrapy
from changenet.items import ChangenetItem

class ChargenetSpider(scrapy.Spider):
    name = 'chargenet'
    allowed_domains = ['bjev520.com']
    url = "http://www.bjev520.com/jsp/beiqi/pcmap/do/pcmap_Detail.jsp?charingId="
    sumer = 2500
    start_urls = [url+str(sumer)]

    def parse(self, response):
	self.sumer +=  1
        new_url = self.url+str(self.sumer)
	item = ChangenetItem()
	i = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/div[@class='news-a']/p)").extract()
	
	print i

	
	#地址
       	adress = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/div[@class='news-a']/p)").extract()[0]
       	#名称
       	name = response.xpath("normalize-space(/html/body/div/div[@class='news-top']/p)").extract()[0]
       	#支付方式
       	pay = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/ul/li[1])").extract()[0]
       	#充电费
       	chargefee = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/ul/li[2])").extract()[0]
       	#服务费
       	servicefee = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/ul/li[3])").extract()[0]
       	#停车费
       	parkingfee = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/ul/li[4])").extract()[0]
       	#开放时间
       	date = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/ul/li[5])").extract()[0]
	#充电桩个数
       	num = response.xpath("normalize-space(/html/body/div/div[@class='news-con']/div[@class='news-c'])").extract()[0]
	if adress.strip()=='':
		yield scrapy.Request(new_url, callback = self.parse)
	else:
		if self.sumer < 20834:
			item['name'] = name.encode('utf-8')
			item['adress'] = adress.encode('utf-8')
			item['pay'] = pay.encode('utf-8')
			item['chargefee'] = chargefee.encode('utf-8')
			item['servicefee'] = servicefee.encode('utf-8')
			item['parkingfee'] = parkingfee.encode('utf-8')
			item['date'] = date.encode('utf-8')
			item['num'] = num.encode('utf-8')
			yield scrapy.Request(new_url, callback = self.parse)
		yield item	
	
