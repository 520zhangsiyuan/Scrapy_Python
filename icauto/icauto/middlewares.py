# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#import logging
#from logging.handlers import RotatingFileHandler
from scrapy import signals
import scrapy
import base64
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
import yaml
from redis import StrictRedis
from icauto.settings import IPPOOL
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
#class IPPOOlS(object):
#    def process_request(self, request, spider):
#	pass	   
#     LOCAL_CONFIG_YAML = '/etc/hq-proxies.yml'
 ##   	with open(LOCAL_CONFIG_YAML, 'r') as f:
   #     	LOCAL_CONFIG = yaml.load(f)
#	redis_db = StrictRedis(
 #               host=LOCAL_CONFIG['REDIS_HOST'], 
  #              port=LOCAL_CONFIG['REDIS_PORT'], 
        #        password=LOCAL_CONFIG['REDIS_PASSWORD'],
   #             db=LOCAL_CONFIG['REDIS_DB']
   #     ) 
#	PROXY_SET = LOCAL_CONFIG['PROXY_SET']
#	proxy = redis_db.srandmember(PROXY_SET)
	#print proxy
 #       if redis_db.sismember(PROXY_SET,proxy):
#		print proxy
  #      	print('使用代理[%s]访问[%s]' % (proxy, request.url))
#	request.meta['proxy'] = 'http://114.107.65.234:4254'
#	return self._retry(request, exception, spider)
class IPPOOlS(HttpProxyMiddleware):
#	pass
    # 初始化
    def __init__(self, ip=''):
     	self.ip = ip
    # 请求处理
    def process_request(self, request, spider):
    # 先随机选择一个IP
    	thisip = random.choice(IPPOOL)
#	thisip = '221.233.44.186:20138'
    	print("当前使用IP是："+ thisip)
    	request.meta["proxy"] = "http://"+thisip
'''
#class MyproxiesSpiderMiddleware(object):
 
#      def __init__(self,ip=''):
#          self.ip=ip
       
#      def process_request(self, request, spider):
#          thisip=random.choice(IPPOOL)
#          print("this is ip:"+thisip["ipaddr"])
#          request.meta["proxy"]="http://"+thisip["ipaddr"]
class ProxyMiddleware(object): 
    # overwrite process request 
    def process_request(self, request, spider): 
        # 设置代理的主机和端口号
        request.meta['proxy'] = "https://114.97.242.53:22791"

        # 设置代理的认证用户名和密码
        proxy_user_pass = "443964544:bhc1h7pl"
        encoded_user_pass = base64.encodestring(proxy_user_pass)

        # 设置代理
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
'''
class MyUserAgentMiddleware(UserAgentMiddleware):
 

    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('MY_USER_AGENT')
        )

    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
	print 'user-Agent' + agent
        request.headers['User-Agent'] = agent
class IcautoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class IcautoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
