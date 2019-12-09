# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import requests

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['demo.com']
    start_urls = ['http://zs.neusoft.edu.cn/pointline.html']

    def getInfo(self, element, value, elementYear, valueYear):  # element: 三个下拉栏 value：下拉栏中的值
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
        driver.maximize_window()
        driver.get('http://zs.neusoft.edu.cn/pointline.html')
        Select(driver.find_element_by_name(element)).select_by_value(value)
        time.sleep(1)
        Select(driver.find_element_by_name(elementYear)).select_by_value(valueYear)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
        time.sleep(1)

    def parse(self, response):
        pass
        


# if __name__ == '__main__':
#