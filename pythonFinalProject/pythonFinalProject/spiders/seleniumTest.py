# from selenium import webdriver
# from urllib.parse import urlencode
# import requests
# import json
# import time
#
# driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.maximize_window()
# driver.get('http://zs.neusoft.edu.cn/pointline.html')
#
#
# def start_requests():
#     base_url = 'http://zs.neusoft.edu.cn/index.php?'
#     ajax_urls = []
#     ajax_url = []
#     for value in getLevelList().values():
#         for value1 in getYearList().values():
#             for value2 in getProvinceList().values():
#                 parm = {
#                     'm': 'pointline',
#                     'c': 'index',
#                     'a': 'public_search',
#                     'cengci': value,
#                     'year': value1,
#                     'prov': value2
#                 }
#                 ajax_urls.append(base_url + urlencode(parm))
#     for i in range(0, len(ajax_urls), 1):
#         ajax_url.append(i)
#     return dict(zip(ajax_url, ajax_urls))
#
#
# def getLevelList():
#     Level = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[1]/select')
#     LevelList = Level.find_elements_by_tag_name('option')
#     levels = []
#     Levels = []
#     for option in LevelList:
#         Levels.append(option.get_attribute('value'))
#
#     for i in range(0, len(Levels), 1):
#         levels.append(i)
#
#     return dict(zip(levels, Levels))
#
#
# def getYearList():
#     Year = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[2]/select')
#     YearList = Year.find_elements_by_tag_name('option')
#     years = []
#     Years = []
#     for option in YearList:
#         Years.append(option.get_attribute('value'))
#
#     for i in range(0, len(Years), 1):
#         years.append(i)
#
#     return dict(zip(years, Years))
#
#
# def getProvinceList():
#     province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
#     provinceList = province.find_elements_by_tag_name('option')
#     provinces = []
#     Provinces = []
#
#     for option in provinceList:
#         Provinces.append(option.get_attribute('value'))
#
#     for i in range(0, len(Provinces), 1):
#         provinces.append(i)
#
#     return dict(zip(provinces, Provinces))
#
#
# def Click():
#     driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
#
#
# def parser():
#     for value in start_requests().values():
#         response = requests.get(value)
#         jsons = response.json()
#         print("理科分数线：")
#         print(jsons.get('show').get('commonli'))
#         print("文科分数线：")
#         print(jsons.get('show').get('commonwen'))
#         print("艺术理：")
#         print(jsons.get('show').get('artli'))
#         print("艺术文：")
#         print(jsons.get('show').get('artwen'))
#         for item in jsons.get('data').items():
#             print(item[1]['zy'])
#             print(item[1]['kl'])
#             print(item[1]['fs'])
#
# if __name__ == '__main__':
#     parser()
# -*- coding: utf-8 -*-
from selenium import webdriver
from urllib.parse import urlencode
from scrapy import Request, Spider

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.get('http://zs.neusoft.edu.cn/pointline.html')


class DemoSpider(object):
    name = 'zs'
    allowed_domains = ['http://zs.neusoft.edu.cn/pointline.html']

    base_url = ['http://zs.neusoft.edu.cn/index.php?']

    # def __init__(self, base_url):
    #     self.base_url = 'http://zs.neusoft.edu.cn/index.php?'
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
                    # url = ''.join(url)
                    url = base_url + str(urlencode(parm))
                    return url

    def parse(self, response):
        pass

if __name__ == '__main__':
    a = DemoSpider()
    print(a.start_requests())
