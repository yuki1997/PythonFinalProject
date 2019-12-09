import time
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.maximize_window()
driver.get('http://zs.neusoft.edu.cn/pointline.html')
time.sleep(1)
Select(driver.find_element_by_name('cengci')).select_by_value('0')
time.sleep(1)
Select(driver.find_element_by_name('year')).select_by_value('2018')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
time.sleep(1)
Select(driver.find_element_by_name('year')).select_by_value('2017')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
time.sleep(1)
Select(driver.find_element_by_name('year')).select_by_value('2016')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
time.sleep(1)
Select(driver.find_element_by_name('cengci')).select_by_value('1')
time.sleep(1)
Select(driver.find_element_by_name('year')).select_by_value('2018')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
time.sleep(1)
Select(driver.find_element_by_name('year')).select_by_value('2017')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
time.sleep(1)
Select(driver.find_element_by_name('year')).select_by_value('2016')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/form/ul/li[4]').click()
time.sleep(1)

options = Select(driver.find_element_by_name('cengci')).all_selected_options
for option in options:
    print('已经被选中的option' + option.text)

years = Select(driver.find_element_by_name('year')).all_selected_options
for year in years:
    print('已经被选中的year' + year.text)

# def getInfo(element, value, elementYear, valueYear):  # element: 三个下拉栏 value：下拉栏中的值
#     # option = webdriver.ChromeOptions()
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
