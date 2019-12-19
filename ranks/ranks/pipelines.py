# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class RanksPipeline(object):
    def process_item(self, item, spider):
        def __init__(self):
            self.conn = pymysql.connect(
                host='localhost',
                user='root',
                password='591586',
                database='zs',
                port=3306,
                charset='utf8'
            )

        def process_item(self, item, spider):
            insert_sql = 'insert into ranks (href) values (%s)'
            try:
                cursor = self.conn.cursor()
                cursor.execute(insert_sql, (item['href']))
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()

            return item

        return item
