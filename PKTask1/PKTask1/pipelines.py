# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#Scrapped Data -> Item Containers -> Pipeline -> SQL/Mongodb atlas


import pymongo
class Pktask1Pipeline():

    def __init__(self):

        self.conn = pymongo.MongoClient(
            'cluster0-shard-00-00.drw2h.mongodb.net:27017',
            27017
        )
        db = self.conn['Kaustubh']
        self.collection = db['Flipkart_tb']


    def process_items(self, items, spider):
        self.collection.insert_one(dict(items))
        return items
