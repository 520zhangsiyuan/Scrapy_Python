#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import base64
import random
import yaml
import MySQLdb
import sys
import time
from redis import StrictRedis
def start_reptile():
	#爬取电桩点信息
	mysqlcli = MySQLdb.connect(host = "192.168.1.26", port = 3306, user = "root", passwd = "root", db = "charges" ,charset="utf8")
	cursor = mysqlcli.cursor()
	LOCAL_CONFIG_YAML = '/etc/hq-proxies.yml'
        with open(LOCAL_CONFIG_YAML, 'r') as f:
                LOCAL_CONFIG = yaml.load(f)
        redis_db = StrictRedis(
                host=LOCAL_CONFIG['REDIS_HOST'],
                port=LOCAL_CONFIG['REDIS_PORT'],
                #password=LOCAL_CONFIG['REDIS_PASSWORD'],
                db=LOCAL_CONFIG['REDIS_DB']
        )
	headers={
	    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    
}
	with open(r"/python/work/test/data.json","r") as f:
	        json_data = f.read()
        	reload(sys)
        	i=1
	        sys.setdefaultencoding( "utf-8" )
        	jd = json.loads(json_data,strict=False)
 #       	filename = open(r"result.txt","wr")
        	#datas =  jd['data'][1]
        	for datas in jd['data']:
                	PROXY_SET = LOCAL_CONFIG['PROXY_SET']
        		proxy = redis_db.smembers(PROXY_SET)
        		proxy = redis_db.sismember(PROXY_SET,proxy)
        		#print('使用代理[%s]访问[%s]' % (proxy, request.url))
			i = i+1
#			time.sleep(0.1)
                	if i < 10600:
                        	continue
                	else:
                        	url = "http://www.echargenet.com/portal/station/info?callback=jQuery191020390295229926436_1531971523453"
                       	 	result = requests.post(url,data=datas,proxies=proxy,headers=headers).text
	                        result1 = result[42:-1].decode('unicode_escape')
        	                json_data = result1.replace('\r', '\\r').replace('\n', '\\n')
                	        print json_data
                        	r1 = json.loads(json_data,strict=False)
				print r1
        	                if r1['data'] is None :
                	               	continue
                       		else:
	                               	#print r1['data']
        	                       	#充电桩名
                	               	name = r1['data']['name'].decode('utf8')           
                        	       	#开放时间
                               		date = r1['data']['businessTime'].decode('utf8')
	                               	#停车费用
        	                       	parkingFee = r1['data']['parkingFee'].decode('utf8')
                	          		#地址
                        	     	adress = r1['data']['address'].decode('utf8')
                               		#服务费
	                               	serviceFee = r1['data']['serviceFee'].decode('utf8')
        	                       	#充电费
                	               	chargingFee = r1['data']['chargingFee'].decode('utf8')
                        	       	#支付方式
                               		payTypeDesc = r1['data']['payTypeDesc'].decode('utf8')
					list1 = second_reptile(datas,proxy,headers).decode('utf8')
					#list1 = ''
					print '(%s, %s, %s, %s, %s, %s, %s, %s)' %(name,adress,list1,chargingFee,serviceFee,payTypeDesc,date,parkingFee)
					sql = "insert into charges (charge_name,charge_address,charge_num,charge_fee,charge_service_fee,charge_pay,charge_date,parking_fee) values ('%s','%s','%s','%s', '%s', '%s', '%s', '%s')"%(name,adress,list1,chargingFee,serviceFee,payTypeDesc,date,parkingFee)
					#print sql
					cursor.execute(sql)	
            				# 提交事务
				        mysqlcli.commit()
            				#关闭游标
		cursor.close()
        	                        #print result_result+'\n'
                	                #filename.write(result_result+'\n')
	#        	filename.close()

   
def second_reptile(datas,proxy,headers):
	#爬取电桩信息
	 url1 = "http://www.echargenet.com/portal/station/chargers?callback=jQuery191020390295229926436_1531971523453"
         result2 = requests.post(url1,data=datas,proxies=proxy,headers=headers).text
         result3 = result2[42:-1].decode('unicode_escape')
	 #print '----------------------------------------------------------------------'
         json_data1 = result3.replace('\r', '\\r').replace('\n', '\\n')        
	 #print json_data1
         r2 = json.loads(json_data1,strict=False)
	 #print r2['data'][0]['chargers']
	 i = 0
	 j = 0
	 list1 = '未知'
	 if r2['data'] is  None:
		return list1
	 else:
		if len(r2['data']) <= 1:
			for data in r2['data'][0]['chargers']:
				chargerType = data['chargerType']
                                print '------------------------------'
                                if chargerType == 'DC':
                                        i +=1
                                elif chargerType == 'AC':
                                        j +=1
		else:
	 	 	for data in r2['data']:
				for data1 in data['chargers']:
					#电桩类型
					#print data1
					print '+++++++++++++++++++++++++++++++++++++++++++++'
					#data = json.loads(data1,strict=False)
					chargerType = data1['chargerType']
					#print '------------------------------'+chargerType
					if chargerType == 'DC':
						i +=1
					elif chargerType == 'AC':
						j +=1
	 list1 = '直流：%d,交流:%d'%(i,j)
	 #print list1
	 return list1
	 

start_reptile()
         		


