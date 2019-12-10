# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
provinceList = province.find_elements_by_tag_name('option')
options = []
for option in provinceList:
    options.append(option.text)
print(options)

class DemoSpider(scrapy.Spider):
    name = 'zs'
    allowed_domains = ['http://zs.neusoft.edu.cn/pointline.html']
    start_urls = ['http://zs.neusoft.edu.cn/pointline.html']

    def getLevelList(self):
        Level = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[1]/select')
        LevelList = Level.find_elements_by_tag_name('option')
        levels = []
        Levels = []
        for option in LevelList:
            Levels.append(option.get_attribute('value'))

        for i in range(0, len(Levels), 1):
            levels.append(i)

        return zip(levels, Levels)

    def getYearList(self):
        Year = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[2]/select')
        YearList = Year.find_elements_by_tag_name('option')
        years = []
        Years = []
        for option in YearList:
            Years.append(option.get_attribute('value'))

        for i in range(0, len(Years), 1):
            years.append(i)

        return zip(years, Years)

    def getProvinceList(self):
        province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
        provinceList = province.find_elements_by_tag_name('option')
        provinces = []
        Provinces = []

        for option in provinceList:
            Provinces.append(option.get_attribute('value'))

        for i in range(0, len(Provinces), 1):
            provinces.append(i)

        return zip(provinces, Provinces)

    def Click(self):
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()

    def parse(self, response):
        pass
