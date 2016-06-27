# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors

class JobPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = 'localhost',
            db = 'catchjob',
            user = 'root',
            passwd = '1234',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = False
        )
    def process_item(self, item, spider):
         item.setdefault('jobname','')
         item.setdefault('companyname','')
         item.setdefault('location','')
         item.setdefault('pay','')
         item.setdefault('time','')
         self.dbpool.runInteraction(self._conditional_insert, item)
         return item


    def _conditional_insert(self, tx, item):
        tx.execute("insert into recruitgis(JobName,CompanyName,Location,Pay,time) values(%s,%s,%s,%s,%s)",
                   (item['jobname'],item['companyname'],item['location'],item['pay'],item['time']))


