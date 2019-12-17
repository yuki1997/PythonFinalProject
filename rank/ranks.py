import requests
from lxml import etree
import pymysql

res = requests.get('https://kaoshi.china.com/gaokao/news/1723427-1.htm')
res.encoding = 'utf-8'
html = etree.HTML(res.text)
href = html.xpath('/html/body/div[3]/div/div[1]/div[3]/ul/li/p/a/@href')

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
    except Exception as e:
        print(e)
        conn.rollback()
conn.close()
