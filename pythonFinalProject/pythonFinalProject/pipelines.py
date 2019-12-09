# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class PythonfinalprojectPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='591586',
            database='zs',
            prot=3306,
            charset='utf8'
        )

    def process_item(self, item, spider):
        insert_sql = 'insert into zsInfo (level, year, province, major, subject, score) values (%s, %s, %s, %s, %s, %s)'
        try:
            cursor = self.conn.cursor()
            cursor.execute(insert_sql, (item['level'],
                                        item['year'],
                                        item['province'],
                                        item['major'],
                                        item['subject'],
                                        item['score']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
