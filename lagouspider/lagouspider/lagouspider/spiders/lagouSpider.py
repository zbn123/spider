#encoding:utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import time
import json
from lagouspider.items import LagouspiderItem
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''
xpath:
1.select,extract,re
2.//;/;[@属性]
3.
'''
class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    # start_urls=["https://www.lagou.com/zhaopin/Python/"+str(2)+"/?filterOption=3"]
    start_urls=[]
    for i in range(28):
        pageNum=i+2
        url="https://www.lagou.com/zhaopin/Python/"+str(pageNum)+"/?filterOption=3"
        start_urls.append(url)

    def parse(self, response):
        # sel = Selector(response)
        # sites = sel.xpath('//ul[@class="item_con_list"]/li[@class="con_list_item default_list"]')
        # contents=sel.xpath("//title/text()").extract()
        # for line in contents:
        #     print line

        hxs=HtmlXPathSelector(response)
        # sites=hxs.select('//ul[@class="item_con_list"]')
        # print hxs.select('//title/text()').extract_unquoted()
        # print hxs.select('//title/text()').extract()
        sites=hxs.select('//ul[@class="item_con_list"]/li[@class="con_list_item default_list"]')
        items = []
        for site in sites:
            # print site.xpath('h2/text()').extract()
            item = LagouspiderItem()
            item['company_name'] = site.select('.//div[@class="company_name"]/a/text()').extract()
            item['company_des'] = site.select('.//div[@class="industry"]/text()').extract()
            item['position_name'] = site.select('.//h2/text()').extract()
            item['publish_time'] = site.select('.//span[@class="format-time"]/text()').extract()
            item['salary'] = site.select('.//div[@class="li_b_l"]/span[@class="money"]/text()').extract()

            # item['company_name'] = site.xpath('.//div[@class="company_name"]/a/text()').extract()
            # item['company_des'] = site.xpath('.//div[@class="industry"]/text()').extract()
            # item['position_name'] = site.xpath('.//h2/text()').extract()
            # item['publish_time'] = site.xpath('.//span[@class="format-time"]/text()').extract()
            # item['salary'] = site.xpath('.//div[@class="li_b_l"]/span[@class="money"]/text()').extract()

            otherCon = site.select('.//div[@class="li_b_l"]/text()').extract()
            print otherCon
            # otherCon2 = site.select('.//div[@class="li_b_l"]/text()').extract()
            # print otherCon2
            # ex_pattern = re.compile(r"\d+-\d+")
            # ed_pattern = re.compile(r'\/')
            # experience = otherCon.re(ex_pattern)
            # education=otherCon.re(ed_pattern)
            # education = re.split(ed_pattern, otherCon)[-1]
            contents=str(otherCon[2]).split("/")
            item["experience"]=contents[0]
            item["education"]=contents[1]
            items.append(item)
        return items
