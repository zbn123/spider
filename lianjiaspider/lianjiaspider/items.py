# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
分析小区都有哪些是属性：
borough_name
borough_avg
cityarea
cityarea2

'''
class LianjiaspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    borough_name=Field()
    borough_detail_link = Field()
    borough_avg=Field()
    cityarea=Field()
    cityarea2=Field()

