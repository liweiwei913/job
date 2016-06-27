# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field

class JobItem(Item):
    jobname=Field(default='')
    companyname=Field(default='')
    location=Field(default='')
    pay=Field(default='')
    time=Field(default='')
    pass
