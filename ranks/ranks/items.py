# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RanksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # province = scrapy.Field()
    href = scrapy.Field()
