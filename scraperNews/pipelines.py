# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from scrapy.exceptions import DropItem


class ScrapernewsPipeline(object):
    def __init__(self):
        self.titles_seen = set()
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('mynews.db')
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS news""")
        self.curr.execute("""CREATE TABLE news (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Title Text NOT NULL)
                    """)

    def store_db(self,item):
        Title = item['Title_new']
        sql = """INSERT INTO news(Title) VALUES("{}")""".format(Title)
        self.curr.execute(sql)
        self.conn.commit()

    def process_item(self, item, spider):
        if item['Title_new'] in self.titles_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.titles_seen.add(item['Title_new'])
            self.store_db(item)
            return item