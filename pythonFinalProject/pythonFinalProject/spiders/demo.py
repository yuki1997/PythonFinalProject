# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['demo.com']
    start_urls = ['http://zs.neusoft.edu.cn/pointline.html']

    def parse(self, response):
        pass
