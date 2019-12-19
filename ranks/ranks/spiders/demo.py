import re

import pymysql
import requests
from lxml import etree
from bs4 import BeautifulSoup

hrefs = []
provinces = []
htmls = []

def DBQuery():
    conn = pymysql.connect(host='localhost',
                       user='root',
                       password='591586',
                       db='zs',
                       charset='utf8')
    cursor = conn.cursor()
    sql = 'select * from 2018href'
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        conn.rollback()
    conn.close()

def get2017Href():
    for row in data:
         res = requests.get(row[0])
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        href = html.xpath('/html/body/div[5]/div[1]/div[3]/div[2]/p[4]/a/@href')
        province = html.xpath('/html/body/div[5]/div[1]/div[2]/div/span/text()')
            if len(href) > 0:
        if len(href[0]) > 42:
            href = href[0][7:49]
            htmls.append(html)
            hrefs.append(href)
            provinces.append(''.join(province))
        else:
            htmls.append(html)
            hrefs.append(''.join(href))
            provinces.append(''.join(province))
    for i in range(0, len(provinces)):
        if i % 2 == 0:
            provinces[i] = provinces[i] + '理科'
        else:
            provinces[i] = provinces[i] + '文科'

if __name__ == '__main__':
    DBQuery()
    get2017Href()
    print(hrefs)
    print(provinces)