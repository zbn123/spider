# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib2
from bs4 import BeautifulSoup
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
'''
1. 可以存储多个文件中或数据库中，需要在setting中配置数据库连接，在从配置中获得；根据字段判断；
2.可以继续爬取串过来的连接，然后使用beautifulsoup解析，然后再组合写入文件中；
'''
class LianjiaspiderPipeline(object):
    def __init__(self):
        self.outputfile=open("beijing_borough.txt","w")
    def process_item(self, item, spider):
        # method1:对应extract()
        # borough_name= item['borough_name'][0] if item['borough_name']!=None else None
        # borough_detail_link=item["borough_detail_link"][0] if item['borough_detail_link']!=None else None
        # borough_avg=item['borough_avg'][0] if item['borough_avg']!=None else None
        # cityarea=item['cityarea'][0] if item['cityarea']!=None else None
        # cityarea2=item['cityarea2'][0] if item['cityarea2']!=None else None
        # writeline =borough_name+","+borough_detail_link+","+borough_avg+","+cityarea+","+cityarea2+"\n"
        #method3:对应extract_first()
        borough_name= item['borough_name']
        borough_detail_link=item["borough_detail_link"]
        borough_avg=item['borough_avg']
        cityarea=item['cityarea']
        cityarea2=item['cityarea2']
        headers={'Host': 'bj.lianjia.com','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'}
        time.sleep(2)
        request = urllib2.Request(borough_detail_link, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()  # 打开文章链接
        soup = BeautifulSoup(html,"lxml")
        img_srcs=soup.find(id="overviewThumbnail").find_all("li")
        for li_src in img_srcs:
            big_src=li_src.attrs["data-src"]
            small_src=li_src.find("img").attrs["src"]
            writeline =borough_name+","+borough_detail_link+","+borough_avg+","+cityarea+","+cityarea2+","+big_src+","+small_src+"\n"
            self.outputfile.write(writeline)

        # method2:
        # self.outputfile.write(json.dumps(dict(item)))
        # self.outputfile.write("\n")
