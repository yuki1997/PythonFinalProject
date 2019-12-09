# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonfinalprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    level = scrapy.Field()
    year = scrapy.Field()
    province = scrapy.Field()
    major = scrapy.Field()
    subject = scrapy.Field()
    score = scrapy.Field()
