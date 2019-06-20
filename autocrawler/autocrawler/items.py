# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AutocrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    model = scrapy.Field()
    version = scrapy.Field()
    body_type = scrapy.Field()
    price = scrapy.Field()
    vat = scrapy.Field()
    km = scrapy.Field()
    registration = scrapy.Field()
    kW = scrapy.Field()
    hp = scrapy.Field()
    url = scrapy.Field()