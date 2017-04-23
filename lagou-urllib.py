#encoding:utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
import re
import time
import json
reload(sys)
sys.setdefaultencoding("utf-8")

outfile=open("position.txt","w+")
def getContent(content):
    btfsp = BeautifulSoup(content, "lxml")
    positions=btfsp.find_all("li",class_="con_list_item default_list")
    num=0
    items=[]
    for position in positions:
        company_name=position.find("div",class_="company_name").find("a").text
        company_des=position.find("div",class_="industry").text
        position_name=position.find("h2").text
        position_detail_link=position.find("a",class_="position_link").get("href")
        time.sleep(2)
        job_detail_html=getPage(position_detail_link)
        job_detail_position = BeautifulSoup(job_detail_html, "lxml")
        position_detail_contents=job_detail_position.find_all("dl",id="job_detail")
        position_addr_str =""
        position_bt_str=""
        for job_detail_content in position_detail_contents:
            if job_detail_content !=None:
                position_advantage=job_detail_content.find("dd",class_="job-advantage").find("p").text
                # print position_advantage
                position_bt=job_detail_content.find("dd",class_="job_bt").find_all("br")
                position_bt2=job_detail_content.find("dd",class_="job_bt").find_all("p")
                position_bt3=job_detail_content.find("dd",class_="job_bt").find_all("span")
                if len(position_bt)!=0:
                    position_bt_true=position_bt
                if len(position_bt2) != 0:
                    position_bt_true = position_bt2
                if len(position_bt3)!=0:
                    position_bt_true=position_bt3
                # position_bt_lists=[]
                for position_bt_item in position_bt_true:
                    # string方法比text好使
                    position_bt_str=position_bt_str+","+str(position_bt_item.string)
                    # position_bt_lists.append(position_bt_item)
                # print position_bt_lists
                # find和findall搭配使用；
                # 也可以用select试试
                position_addrs=job_detail_content.find("dd",class_="job-address clearfix").find_all("a")
                # 不要用数组，否则会产生中文变为unicode类型串
                # position_addr_lists=[]

                for position_addr in position_addrs:
                    position_addr_str=position_addr_str+","+str(position_addr.string)
                    # position_addr_lists.append(position_addr.text)
        print position_bt_str
        print type(position_addr_str)
        # print "===",position_bt_lists
        # print "@@@",position_addr_lists
        publish_time=position.find("span",class_="format-time").text
        salary=position.find("div",class_="li_b_l").find("span",class_="money").text
        otherCon=position.find("div",class_="li_b_l").text
        ex_pattern=re.compile(r"\d+-\d+")
        ed_experience=re.compile(r"/")
        experience=re.findall(ex_pattern,otherCon)
        education=re.split(ed_experience,otherCon)[-1]
        write_line=str(company_name).strip().strip("\n")+"@"+str(company_des).strip().strip("\n")+"@"+str(position_name).strip().strip("\n")+"@"+str(publish_time).strip().strip("\n")+"@"+str(salary).strip().strip("\n")+"@"+str(experience)[3:-2]+"@"+str(education).strip().strip("\n")+"@"+str(position_advantage).strip().strip("\n")+"@"+position_bt_str.strip().strip("\n")+"@"+position_addr_str.strip().strip("\n")

        outfile.write(write_line)
        outfile.write("\n")
        outfile.flush()
        # items.append(company_name)
        # items.append(company_des)
        # items.append(position_name)
        # items.append(publish_time)
        # items.append(experience)
        # items.append(education)
        # return items
def getPage(url):
    headers={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
             "Host":"www.lagou.com"}
    request=urllib2.Request(url,headers=headers)
    response= urllib2.urlopen(request)
    html=response.read()
    return html

def start():
    # url="https://www.lagou.com/zhaopin/Python/"+str(2)+"/?filterOption=3"

    for i in range(28):
        pageNum=i+2
        url="https://www.lagou.com/zhaopin/Python/"+str(pageNum)+"/?filterOption=3"
        html=getPage(url)
        getContent(html)
        time.sleep(6)

if __name__=="__main__":
    start()