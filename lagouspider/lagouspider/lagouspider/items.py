# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class LagouspiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = Field()
    company_des = Field()
    position_name = Field()
    publish_time = Field()
    salary = Field()
    experience=Field()
    education=Field()

