#encoding:utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import time
import json
from lianjiaspider.items import LianjiaspiderItem
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''
xpath:
1.select,extract,re
2.//;/;[@属性];/@title/@name/@href/[@class=""]/[@id=""]
3.extract_first()/extract/
4.在这里可以实现翻页的功能；
5. Call to deprecated function select. Use .xpath() instead.
'''
class DmozSpider(Spider):

    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    # start_urls=["http://bj.lianjia.com/xiaoqu/"]
    start_urls=[]
    for i in range(100):
        pageNum=i+1
        if pageNum==1:
            url="http://bj.lianjia.com/xiaoqu/"
        else:
            url="http://bj.lianjia.com/xiaoqu/pg"+str(pageNum)+"/"
        start_urls.append(url)

    def parse(self, response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//ul[@class="listContent"]/li[@class="clear xiaoquListItem"]')
        items = []
        for site in sites:
            item = LianjiaspiderItem()
            # item['borough_name'] = site.select('.//div[@class="title"]/a/text()').extract()
            # item["borough_detail_link"]=site.select('.//div[@class="title"]/a/@href').extract()
            # item['borough_avg'] = site.select('.//div[@class="totalPrice"]/span/text()').extract()
            # item['cityarea'] = site.select('.//div[@class="positionInfo"]/a[@class="district"]/text()').extract()
            # item['cityarea2'] = site.select('.//div[@class="positionInfo"]/a[@class="bizcircle"]/text()').extract()

            item['borough_name'] = site.select('.//div[@class="title"]/a/text()').extract_first()
            item["borough_detail_link"]=site.select('.//div[@class="title"]/a/@href').extract_first()
            item['borough_avg'] = site.select('.//div[@class="totalPrice"]/span/text()').extract_first()
            item['cityarea'] = site.select('.//div[@class="positionInfo"]/a[@class="district"]/text()').extract_first()
            item['cityarea2'] = site.select('.//div[@class="positionInfo"]/a[@class="bizcircle"]/text()').extract_first()
            items.append(item)
        return items
