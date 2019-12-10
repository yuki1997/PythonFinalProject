from selenium import webdriver
from urllib.parse import urlencode
import requests
import json
import time

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.get('http://zs.neusoft.edu.cn/pointline.html')


def start_requests():
    base_url = 'http://zs.neusoft.edu.cn/index.php?'
    ajax_urls = []
    ajax_url = []
    for value in getLevelList().values():
        for value1 in getYearList().values():
            for value2 in getProvinceList().values():
                parm = {
                    'm': 'pointline',
                    'c': 'index',
                    'a': 'public_search',
                    'cengci': value,
                    'year': value1,
                    'prov': value2
                }
                ajax_urls.append(base_url + urlencode(parm))
    for i in range(0, len(ajax_urls), 1):
        ajax_url.append(i)
    return dict(zip(ajax_url, ajax_urls))


def getLevelList():
    Level = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[1]/select')
    LevelList = Level.find_elements_by_tag_name('option')
    levels = []
    Levels = []
    for option in LevelList:
        Levels.append(option.get_attribute('value'))

    for i in range(0, len(Levels), 1):
        levels.append(i)

    return dict(zip(levels, Levels))


def getYearList():
    Year = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[2]/select')
    YearList = Year.find_elements_by_tag_name('option')
    years = []
    Years = []
    for option in YearList:
        Years.append(option.get_attribute('value'))

    for i in range(0, len(Years), 1):
        years.append(i)

    return dict(zip(years, Years))


def getProvinceList():
    province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
    provinceList = province.find_elements_by_tag_name('option')
    provinces = []
    Provinces = []

    for option in provinceList:
        Provinces.append(option.get_attribute('value'))

    for i in range(0, len(Provinces), 1):
        provinces.append(i)

    return dict(zip(provinces, Provinces))


def Click():
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()


def parser():
    for value in start_requests().values():
        response = requests.get(value)
        json = response.json()
        data = json.get('data')

        if data != None:
            print(data)


if __name__ == '__main__':
    parser()
