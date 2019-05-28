# -*- coding: utf-8 -*-
import re
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MysqlPipeline(object):
    def process_item(self, item, spider):
        item=dict(item)
        print(item)
        def table_exists(conn, table_name):
            sql = "show tables;"
            conn.execute(sql)
            tables = [conn.fetchall()]
            table_list = re.findall('(\'.*?\')', str(tables))
            table_list = [re.sub("'", '', each) for each in table_list]
            if table_name in table_list:
                return 1
            else:
                return 0
        self.conn= pymysql.connect(host='localhost',user='root',password='8911980',port=3306,db='test')
        self.cursor = self.conn.cursor()
        table_name = 'lianjia_huairou'
        if (table_exists(self.cursor, table_name) != 1):
            self.cursor.execute('create table lianjia_huairou( url varchar(100),title varchar(200),location varchar(100),year varchar(100),xiaoqu varchar(100),followInfo varchar(100),daikan varchar(100),subway varchar(100),taxfree varchar(100),totalPrice double(7,2),unitPrice varchar(100),region varchar(60),fangjian varchar(100),quare varchar(100),direction varchar(100),zhuangxiu varchar(200),dianti varchar(100),positionInfo varchar(100)) ENGINE=InnoDB DEFAULT character set utf8mb4 collate utf8mb4_general_ci;')
        self.cursor.execute("insert into lianjia_huairou( url,title,location,year,xiaoqu,followInfo,daikan,subway,taxfree,totalPrice,unitPrice,region,fangjian,quare,direction,zhuangxiu,dianti,positionInfo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['url'],item['title'],item['location'],item['year'],item['xiaoqu'],item['followInfo'],item['daikan'],item['subway'],item['taxfree'],item['totalPrice'],item['unitPrice'],item['region'],item['fangjian'],item['quare'],item['direction'],item['zhuangxiu'],item['dianti'],item['positionInfo']))


        self.conn.commit()
        self.cursor.close()
        self.conn.close()

