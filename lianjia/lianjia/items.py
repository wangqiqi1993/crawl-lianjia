# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    url=scrapy.Field()
    title=scrapy.Field()
    location=scrapy.Field()
    fangjian= scrapy.Field()
    quare= scrapy.Field()
    direction = scrapy.Field()
    zhuangxiu= scrapy.Field()
    dianti= scrapy.Field()
    positionInfo=scrapy.Field()
    year=scrapy.Field()
    xiaoqu=scrapy.Field()
    followInfo=scrapy.Field()
    daikan=scrapy.Field()
    subway=scrapy.Field()
    taxfree=scrapy.Field()
    totalPrice=scrapy.Field()
    unitPrice=scrapy.Field()
    region=scrapy.Field()
