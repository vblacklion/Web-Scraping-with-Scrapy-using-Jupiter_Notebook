# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class AutocrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    make_model = Field()
    short_description = Field()
    body_type = Field()
    price = Field()
    vat = Field()
    km = Field()
    registration = Field()
    kW = Field()
    hp = Field()
    url = Field()
    
    
#class Website(Item):
#   def __setitem__(self, key, value):
#       if key not in self.fields:
#           self.fields[key] = Field()
#       self._values[key] = value
        
        