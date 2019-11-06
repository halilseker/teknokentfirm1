# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import sqlite3


class MongodbPipeline(object):
    collection_name = "sautekfirm3"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(
            "mongodb+srv://hiseker:adiyla83bit@cluster0-fj10c.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["TEKNOKENT"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item


class SQLlitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("sakaryateknokent.db")
        self.c = self.connection.cursor()
        self.c.execute('''
            CREATE TABLE sautekfirm3(
                firm_title TEXT,
                firm_representative TEXT,
                firm_phone_number TEXT,
                firm_email TEXT,
                firm_address TEXT,
                firm_services TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO sautekfirm3 (firm_title, firm_representative, firm_phone_number, firm_email, firm_address, firm_services) VALUES(?,?,?,?,?,?)
        
        ''', (
            item.get('firm_title'),
            item.get('firm_representative'),
            item.get('firm_phone_number'),
            item.get('firm_email'),
            item.get('firm_address'),
            item.get('firm_services'),
        ))
        self.connection.commit()
        return item
