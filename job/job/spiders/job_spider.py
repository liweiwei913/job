__author__ = 'liweiwei'


import sys
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

from job.items import JobItem

class Job_Spider(Spider):
    reload(sys)
    name = 'job_spider'
    start_urls=[]
    for i in range(1,95):
        url='http://search.51job.com/jobsearch/search_result.php?&keyword=GIS&curr_page=%d' %(i)
        start_urls.append(url)

    def parse(self, response):
        print response.url
        div = response.xpath("//div[@id='resultList']/div[@class='el']")
        for j in range(0,len(div)):
            item =JobItem()
            jobname=response.xpath("//div[@class='el']/p/span/a/@title").extract()[j]
            companyname=response.xpath("//div[@class='el']/span[@class='t2']/a/@title").extract()[j]
            location=response.xpath("//div[@class='el']/span[@class='t3']/text()").extract()[j]
            pay=response.xpath("//div[@class='el']/span[@class='t4']").extract()[j]
            time=response.xpath("//div[@class='el']/span[@class='t5']/text()").extract()[j]
            item['jobname'] = jobname
            item['companyname'] = companyname
            item['location'] = location
            item['pay'] = pay[17:-7]
            item['time'] = time
            yield item
