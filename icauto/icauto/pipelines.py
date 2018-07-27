# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.utils.project import get_project_settings
import pymysql

class IcautoPipeline(object):
    
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.pwd = settings['DB_PWD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             password=self.pwd,
                             db=self.name,
                             charset=self.charset)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()

    def process_item(self, item, spider):
        sql = "insert into charges(charge_name,charge_address,charge_num,charge_fee,charge_service_fee,charge_pay,charge_date,parking_fee,charge_abstract) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" %(item['name'],item['adress'],item['num'],item['chargefee'],item['servicefee'],item['pay'],item['date'],item['parkingfee'],item['cdz'])
        # 执行sql语句
        self.cursor.execute(sql)
        self.conn.commit()
        return item

