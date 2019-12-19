import re
import pymysql
import requests
from lxml import etree
from bs4 import BeautifulSoup

hrefs = []
provinces = []
htmls = []

#
# def DBQuery():
#     conn = pymysql.connect(host='localhost',
#                            user='root',
#                            password='591586',
#                            db='zs',
#                            charset='utf8')
#     cursor = conn.cursor()
#     sql = 'select href from 2018href'
#     try:
#         cursor.execute(sql)
#         data = cursor.fetchall()
#     except Exception as e:
#         print(e)
#         conn.rollback()
#     conn.close()
#     return data
#

def get2018Href():
    res = requests.get('https://kaoshi.china.com/gaokao/news/1723427-1.htm')
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    hrefs = html.xpath('/html/body/div[3]/div/div[1]/div[3]/ul/li/p/a/@href')
    hrefs.remove('https://www.thea.cn/xgkfd_zx_1695963-1.htm')
    hrefs.remove('https://www.thea.cn/xgkfd_zx_1695976-1.htm')
    for href in hrefs:
        res = requests.get(href)
        res.encoding = 'utf-8'
        html = etree.HTML(res.text)
        province = html.xpath('/html/body/div[5]/div/div[2]/div/span/text()')
        provinces.append(''.join(province))
        # print(province)
    for i in range(0, len(provinces)):
        if i % 2 == 0:
            provinces[i] = provinces[i] + '理科'
        else:
            provinces[i] = provinces[i] + '文科'

    return dict(zip(provinces, hrefs))


def dicToSql(dic, sql):
    sf = ''
    for key in dic:
        tup = (key, dic[key])
        sf += (str(tup) + ',')
    sf = sf.rstrip(',')

    sql2 = sql % sf
    return sql2


def DBInsert():

    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='591586',
                            db='zs',
                            charset='utf8')
    cursor = conn.cursor()
    sql = 'insert into 2018href(province, href) values %s;'
    ret = dicToSql(get2018Href(), sql)
    cursor.execute(ret)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    DBInsert()
