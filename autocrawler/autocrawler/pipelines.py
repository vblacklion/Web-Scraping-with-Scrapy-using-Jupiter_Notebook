# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from scrapy_sci.status import Status, Reader

class AutocrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class CleaningPipeline(object):

    def process_item(self, item, spider):
        
        item['price'] = int(''.join(filter(str.isdigit, item['price'])))
            
        return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item    
    
#class JsonWriterPipeline(object):

#    def open_spider(self, spider):
#        self.file = open('items.jl', 'w')

#    def close_spider(self, spider):
#        self.file.close()

#    def process_item(self, item, spider):
#        line = json.dumps(dict(item)) + "\n"
#        self.file.write(line)
#        return item

#class DuplicatesPipeline(object):

#    def __init__(self):        
#        self.ids_seen = set()
#        status = Status()
#        for classifier in status.classifiers.keys():
#            for rf in status.classifiers[classifier]['reviewed']:
#                json = Reader.read_reviewed(rf)
#                self.ids_seen.add(json['origin'])

#    def process_item(self, item, spider):
#        if item['origin'] in self.ids_seen:
#            raise DropItem("Duplicate item found: %s" % item)
#        else:
#            self.ids_seen.add(item['origin'])
#            return item
