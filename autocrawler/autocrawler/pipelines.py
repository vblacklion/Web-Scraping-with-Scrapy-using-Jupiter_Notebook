# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy_sci.status import Status, Reader

class AutocrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


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
