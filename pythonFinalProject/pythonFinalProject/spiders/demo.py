# -*- coding: utf-8 -*-
import json

import scrapy
from selenium import webdriver
from urllib.parse import urlencode
from scrapy import Request, Spider

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.get('http://zs.neusoft.edu.cn/pointline.html')


class DemoSpider(scrapy.Spider):
    name = 'zs'
    allowed_domains = ['http://zs.neusoft.edu.cn/pointline.html']
    start_urls = ['http://zs.neusoft.edu.cn/pointline.html']
    base_url = ['http://zs.neusoft.edu.cn/index.php?']

    def getLevelList(self):
        Level = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[1]/select')
        LevelList = Level.find_elements_by_tag_name('option')
        levels = []
        Levels = []
        for option in LevelList:
            Levels.append(option.get_attribute('value'))

        for i in range(0, len(Levels), 1):
            levels.append(i)

        return dict(zip(levels, Levels))

    def getYearList(self):
        Year = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[2]/select')
        YearList = Year.find_elements_by_tag_name('option')
        years = []
        Years = []
        for option in YearList:
            Years.append(option.get_attribute('value'))

        for i in range(0, len(Years), 1):
            years.append(i)

        return dict(zip(years, Years))

    def getProvinceList(self):
        province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
        provinceList = province.find_elements_by_tag_name('option')
        provinces = []
        Provinces = []

        for option in provinceList:
            Provinces.append(option.get_attribute('value'))

        for i in range(0, len(Provinces), 1):
            provinces.append(i)

        return dict(zip(provinces, Provinces))

    def start_requests(self):
        base_url = ''.join(self.base_url)
        for value in self.getLevelList().values():
            for value1 in self.getYearList().values():
                for value2 in self.getProvinceList().values():
                    parm = {
                        'm': 'pointline',
                        'c': 'index',
                        'a': 'public_search',
                        'cengci': value,
                        'year': value1,
                        'prov': value2
                    }
                    # url.append(base_url + str(urlencode(parm)))
                    url = base_url + str(urlencode(parm))
                    return url
                    yield Request(url=url, callback=self.parse)

    def parse(self, response):
        jsons = json.loads(response.body)
        print(response)
        # print(self.start_requests())
        # print("理科分数线：")
        # print(jsons.get('show').get('commonli'))
        # print("文科分数线：")
        # print(jsons.get('show').get('commonwen'))
        # print("艺术理：")
        # print(jsons.get('show').get('artli'))
        # print("艺术文：")
        # print(jsons.get('show').get('artwen'))
        #
        # # if jsons.get('data') is not None:
        # print(jsons.get('data').get('zy'))
        # print(jsons.get('data').get('kl'))
        # print(jsons.get('data').get('fs'))
