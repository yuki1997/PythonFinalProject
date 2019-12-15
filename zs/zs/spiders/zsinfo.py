# -*- coding: utf-8 -*-
import json

import scrapy
from selenium import webdriver
from urllib.parse import urlencode
from urllib import parse
from scrapy import Request, Spider
import jsonpath
from zs.items import ZsItem

driver = webdriver.Firefox(executable_path='C:\geckodriver.exe')
driver.get('http://zs.neusoft.edu.cn/pointline.html')


class Zsinfo(scrapy.Spider):
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
                    yield Request(url=url, callback=self.parse)

    def parse(self, response):
        jsons = json.loads(response.body)
        major = []
        subject = []
        score = []

        item = ZsItem()
        if jsons.get('show').get('commonli') != 0 or jsons.get('show').get('commonwen') != 0 or jsons.get('show').get(
                'artli') != 0 or jsons.get('show').get('artwen') != 0:
            params = parse.parse_qs(parse.urlparse(response.request.url).query)
            cengci = params['cengci'].pop()
            year = params['year'].pop()
            prov = params['prov'].pop()
            dictInfo = dict(zip(['cengci', 'year', 'prov'], [cengci, year, prov]))
            scoreInfo = jsons.get('show')
            # print(jsons.get('data'))
            key = ['major', 'subject', 'score']
            majorList = []
            subjectList = []
            # majorList = jsonpath.jsonpath(jsons, '$..zy')
            # subjectList = jsonpath.jsonpath(jsons, '$..kl')
            # scoreList = jsonpath.jsonpath(jsonpath, '$.data..fs')
            fsList = []
            # print(majorList)
            # print(subjectList)
            # print(scoreList)

            '''json test'''
            mask = jsons['data']
            for zidian in mask:
                majorList.append(mask[zidian]['zy'])
                majorList.append(mask[zidian]['kl'])
                majorList.append(mask[zidian]['fs'])

            for i in range(0, len(majorList), 3):
                scoreList = majorList[i: i + 3]
                print(scoreList)

            '''test end'''
            item['level'] = dictInfo['cengci']
            item['year'] = dictInfo['year']
            item['province'] = dictInfo['prov']
            item['ScienceScoreLine'] = scoreInfo['commonli']
            item['LiberalArtsScoreLine'] = scoreInfo['commonwen']
            item['ArtScience'] = scoreInfo['artli']
            item['ArtLiberalArt'] = scoreInfo['artwen']
            #
            # item['major'] = majorList.pop()
            # item['subject'] = subjectList.pop()
            # item['score'] = fsList.pop()
            yield item
