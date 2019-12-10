import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pyquery import PyQuery as pq

# doc = pq('http://zs.neusoft.edu.cn/pointline.html')
# provinces = doc('select')('#prov').text()
# print(provinces)

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.get('http://zs.neusoft.edu.cn/pointline.html')


# province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
# provinceList = province.find_elements_by_tag_name('option')
# options = []
# for option in provinceList:
#     options.append(option.text)
# print(options)
# driver.close()


def getLevelList():
    Level = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[1]/select')
    LevelList = Level.find_elements_by_tag_name('option')
    levels = []
    Levels = []
    for option in LevelList:
        Levels.append(option.get_attribute('value'))

    for i in range(0, len(Levels), 1):
        levels.append(i)

    return zip(levels, Levels)


def getYearList():
    Year = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[2]/select')
    YearList = Year.find_elements_by_tag_name('option')
    years = []
    Years = []
    for option in YearList:
        Years.append(option.get_attribute('value'))

    for i in range(0, len(Years), 1):
        years.append(i)

    return zip(years, Years)


def getProvinceList():
    province = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')
    provinceList = province.find_elements_by_tag_name('option')
    provinces = []
    Provinces = []

    for option in provinceList:
        Provinces.append(option.get_attribute('value'))

    for i in range(0, len(Provinces), 1):
        provinces.append(i)

    return zip(provinces, Provinces)


def Click():
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()


if __name__ == '__main__':
    for key, value in getLevelList():
        for key1, value1 in getYearList():
            for key2, value2 in getProvinceList():
                Select(driver.find_element_by_name('cengci')).select_by_value(value)
                Select(driver.find_element_by_name('year')).select_by_value(value1)
                Select(driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[3]/select')).select_by_value(value2)
                Click()
                time.sleep(1)
    driver.close()

# time.sleep(1)
# Select(driver.find_element_by_name('cengci')).select_by_value('0')
# time.sleep(1)
# Select(driver.find_element_by_name('year')).select_by_value('2018')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
# time.sleep(1)
# Select(driver.find_element_by_name('year')).select_by_value('2017')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
# time.sleep(1)
# Select(driver.find_element_by_name('year')).select_by_value('2016')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
# time.sleep(1)
# Select(driver.find_element_by_name('cengci')).select_by_value('1')
# time.sleep(1)
# Select(driver.find_element_by_name('year')).select_by_value('2018')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
# time.sleep(1)
# Select(driver.find_element_by_name('year')).select_by_value('2017')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
# time.sleep(1)
# Select(driver.find_element_by_name('year')).select_by_value('2016')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
# time.sleep(1)
#
# options = Select(driver.find_element_by_name('cengci')).all_selected_options
# for option in options:
#     print('已经被选中的option' + option.text)
#
# years = Select(driver.find_element_by_name('year')).all_selected_options
# for year in years:
#     print('已经被选中的year' + year.text)

# def getInfo(element, value, elementYear, valueYear):  # element: 三个下拉栏 value：下拉栏中的值
#     option = webdriver.ChromeOptions()
#     # option.add_argument('headless')
#     driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
#     driver.maximize_window()
#     driver.get('http://zs.neusoft.edu.cn/pointline.html')
#     Select(driver.find_element_by_name(element)).select_by_value(value)
#     time.sleep(1)
#     Select(driver.find_element_by_name(elementYear)).select_by_value(valueYear)
#     time.sleep(1)
#     driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
#     time.sleep(1)
#
# if __name__ == '__main__':
#     getInfo('cengci', '0', 'year', '2018')
#     getInfo('cengci', '1', 'year', '2017')
