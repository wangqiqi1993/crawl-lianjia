# -*- coding: utf-8 -*-
import scrapy
import re
import time
from lianjia.items import LianjiaItem
class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    NOT_EXIST_STR = ''
    NOT_EXIST_NUM = -1
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['http://bj.lianjia.com/']
    base_url = 'https://bj.lianjia.com/ershoufang/{region}/pg{page}/'
    regions=[
        'huairou'
    ]

    Max_page=100
    def start_requests(self):
        for region in self.regions:
            for page in range(1,self.Max_page+1):
                url=self.base_url.format(region=region,page=page)
                try:
                    yield scrapy.Request(url=url,callback=self.parse)
                except:
                    print('Get anything')
    def parse(self, response):
        region=response.url.split('/')[-3]
        results=re.findall('<a class="noresultRecommend img ".*?<li class="clear LOGCLICKDATA" >',response.text)
        for result in results:
            item=LianjiaItem()
            try:
                item['url']=re.findall('<a class="noresultRecommend img " href="(.*?)"',result)[0]
            except:
                item['url'] =''
            try:
                item['title']=re.findall('<a class="noresultRecommend img " href=.*?alt="(.*?)"',result)[0]
            except:
                item['title'] =''
            try:
                item['location']=re.findall('<a class="noresultRecommend img " href=.*?alt=.*?data-el="region">(.*?)</a>',result)[0]
            except:
                item['location'] =''
            try:
                info=re.findall('<a class="noresultRecommend img " href=.*?alt=.*?data-el="region">.*?</a><span class="divide">/</span>(.*?)<span class="divide">/</span>(.*?平米)<span class="divide">/</span>(.*?)<span class="divide">/</span>(.*?)<span class="divide">/</span>(.*?)</div>',result)[0]
                try:
                    item['fangjian']=info[0]
                except:
                    item['fangjian'] =''
                try:
                    item['quare']=info[1]
                except:
                    item['quare'] =''
                try:
                    item['direction']=info[2]
                except:
                    item['direction'] =''
                try:
                    item['zhuangxiu']=info[3]
                except:
                    item['zhuangxiu'] =''
                try:
                    item['dianti']=info[4]
                except:
                    item['dianti'] =''
            except:
                item['fangjian'] = ''
                item['square'] = ''
                item['direction'] = ''
                item['zhuangxiu'] = ''
                item['dianti'] = ''
            try:
                item['positionInfo']=re.findall('<div class="positionInfo">(.*?)<span',result)[0]
            except:
                item['positionInfo'] =''
            try:
                item['year']=re.findall('<div class="positionInfo">.*?<span class="divide">/</span>(.*?)<span class="divide">/</span>',result)[0]
            except:
                item['year'] =''
            try:
                item['xiaoqu']=re.findall('<a.*?target="_blank">(.*?)</a>',result)[0]
            except:
                item['xiaoqu'] =''
            try:
                item['followInfo']=re.findall('<div class="followInfo">(.*?关注)<span',result)[0]
            except:
                item['followInfo'] =''
            try:
                item['daikan']=re.findall('<div class="followInfo">.*?<span class="divide">/</span>(.*)<div class="tag">',result)[0]
            except:
                item['daikan'] =''
            try:
                item['subway']=re.findall('<span class="subway">(.*?)</span>',result)[0]
            except:
                item['subway'] =''
            try:
                item['taxfree']=re.findall('<span class="taxfree">(.*?)</span>',result)[0]
            except:
                item['taxfree'] =''
            try:
                item['totalPrice']=re.findall('<div class="totalPrice"><span>(.*?)</span>.*?</div>',result)[0]
            except:
                item['totalPrice'] =-1
            try:
                item['unitPrice']=re.findall('<div class="unitPrice".*?><span>(.*?)</span>',result)[0]
            except:
                item['unitPrice'] =''
            item['region']=region
            yield item




