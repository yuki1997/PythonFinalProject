import requests
from lxml import etree
import pymysql

res = requests.get('https://kaoshi.china.com/gaokao/news/1723427-1.htm').text
html = etree.HTML(res)
href = html.xpath('/html/body/div[3]/div/div[1]/div[3]/ul/li/p/a/@href')
print(href)
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='591586',
                       db='zs',
                       charset='utf8')
cursor = conn.cursor()
for i in range(0, len(href)):
    sql = 'insert into rankHref(href) values(%s)'
    try:
        cursor.execute(sql, href[i])
        conn.commit()
    except:
        conn.rollback()
conn.close()

