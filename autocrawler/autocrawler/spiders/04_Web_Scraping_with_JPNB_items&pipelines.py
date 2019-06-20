# -*- coding: utf-8 -*-
# Importing scrapy
import scrapy
#from scrapy.crawler import CrawlerProcess
# Defining the spider class
# MMWD: Multiple Models With Details

# import items from items.py

from autocrawler.items import AutocrawlerItem

class ScoutAutoCrawler(scrapy.Spider):
    
    name = "scout_mmwd"
    
    allowed_domains = ["autoscout24.com"]
    
    def start_requests( self ):         
        page_number = 1
        base_url = "https://www.autoscout24.com/"
        makes = ['cupra', 'other',]
        #models = {"audi" : ['a4', 'a6', 'a5'],
        #          "opel" : ['corsa', 'adam', 'meriva'],
        #          "renault" : ['clio', 'duster', 'scenic']
        #          }
        #years = ["2014", "2015"]
        #desc = ["0", "1"]
        #gear = ["A", "M", "S"]
        
        
        #for i in range(3):
        #    l = len(models[makes[i]])
        #    for x in range(l):
        #        for y in range(2):
        #            for a in range(2):
        #                for g in range(3):
        #                    for page_number in range(1,21):
        #                
        #                        url = base_url+"lst/"+makes[i]+"/"+models[makes[i]][x]+"?sort=price&\
        #                        desc="+desc[a]+"&gear="+gear[g]+"&ustate=N%2CU&size=20&page="+str(page_number)+"&\
        #                        fregto="+years[y]+"&fregfrom="+years[y]+"&atype=C&"
        
        for i in range(2):
            for page_number in range(1,21):
                url = base_url + "lst/cupra/" + makes[i] + "?sort=price&desc=0&ustate=N%2CU&size=20\
                &page=" + str(page_number) + "1&atype=C&"
        
                yield scrapy.Request( url = url, dont_filter = False, callback = self.parse) 
    

    def parse(self, response):
        
        base_url = "https://www.autoscout24.com/"
        all_auto_divs = response.css(".cldt-summary-full-item-main")
        
        for auto_divs in all_auto_divs:
            
            #advertisement details link finder
            detail_page = auto_divs.css(".cldt-summary-titles")
            link = detail_page.css('a::attr(href)').extract_first()          
        
            yield scrapy.Request( url = base_url+link, callback = self.parse_details)
        
    
    def parse_details(self, response):
        
        items = AutocrawlerItem()
        
        headline = response.css(".cldt-headline")
        make_model = headline.css("h1.cldt-detail-title > span:nth-child(1) ::text").extract_first()
        short_description = headline.css("h1.cldt-detail-title > span:nth-child(2) ::text").extract_first()
        body_type = headline.css("h4.cldt-detail-subheadline ::text").extract_first()
        
        stage = response.css(".cldt-stage-data")
        price = stage.css("div.cldt-price > h2 ::text").extract_first()
        vat = stage.css("div.cldt-stage-headline > div:nth-child(2) > p > span ::text").extract()
        km = stage.css("div.cldt-stage-basic-data > div:nth-child(1) > span ::text").extract()
        registration = stage.css("div.cldt-stage-basic-data > div:nth-child(2) > span ::text").extract()
        kW = stage.css("div.cldt-stage-basic-data > div:nth-child(3) > span:nth-child(1) ::text").extract()
        hp = stage.css("div.cldt-stage-basic-data > div:nth-child(3) > span:nth-child(2) ::text").extract()
        
        items["url"] = response.url
        
        Details = response.css("div.cldt-item[data-item-name='car-details']")
        details = Details.css("div.sc-grid-row > div:nth-child(1)")
        #details
        state_1 = details.css("div:nth-child(1) > dl > dt:nth-child(1) ::text").extract_first()
        state_2 = details.css("div:nth-child(1) > dl > dd:nth-child(2) ::text").extract()
        
        state_3 = details.css("div:nth-child(1) > dl > dt:nth-child(3) ::text").extract_first()
        state_4 = details.css("div:nth-child(1) > dl > dd:nth-child(4) ::text").extract()
        
        state_5 = details.css("div:nth-child(1) > dl > dt:nth-child(5) ::text").extract_first()
        state_6 = details.css("div:nth-child(1) > dl > dd:nth-child(6) ::text").extract()
        
        state_7 = details.css("div:nth-child(1) > dl > dt:nth-child(7) ::text").extract_first()
        state_8 = details.css("div:nth-child(1) > dl > dd:nth-child(8) ::text").extract()
        
        state_9 = details.css("div:nth-child(1) > dl > dt:nth-child(9) ::text").extract_first()
        state_10 = details.css("div:nth-child(1) > dl > dd:nth-child(10) ::text").extract()
        
        state_11 = details.css("div:nth-child(1) > dl > dt:nth-child(11) ::text").extract_first()
        state_12 = details.css("div:nth-child(1) > dl > dd:nth-child(12) ::text").extract()
        
        state_13 = details.css("div:nth-child(1) > dl > dt:nth-child(13) ::text").extract_first()
        state_14 = details.css("div:nth-child(1) > dl > dd:nth-child(14) ::text").extract()
        
        state_15 = details.css("div:nth-child(1) > dl > dt:nth-child(15) ::text").extract_first()
        state_16 = details.css("div:nth-child(1) > dl > dd:nth-child(16) ::text").extract()
        
        state_17 = details.css("div:nth-child(1) > dl > dt:nth-child(17) ::text").extract_first()
        state_18 = details.css("div:nth-child(1) > dl > dd:nth-child(18) ::text").extract()
        
        state_19 = details.css("div:nth-child(1) > dl > dt:nth-child(19) ::text").extract_first()
        state_20 = details.css("div:nth-child(1) > dl > dd:nth-child(20) ::text").extract()
        
        #properties
        properties_1 = details.css("div:nth-child(2) > dl > dt:nth-child(1) ::text").extract_first()
        properties_2 = details.css("div:nth-child(2) > dl > dd:nth-child(2) ::text").extract()
        
        properties_3 = details.css("div:nth-child(2) > dl > dt:nth-child(3) ::text").extract_first()        
        properties_4 = details.css("div:nth-child(2) > dl > dd:nth-child(4) ::text").extract()

        properties_5 = details.css("div:nth-child(2) > dl > dt:nth-child(5) ::text").extract_first()        
        properties_6 = details.css("div:nth-child(2) > dl > dd:nth-child(6) ::text").extract()

        properties_7 = details.css("div:nth-child(2) > dl > dt:nth-child(7) ::text").extract_first()        
        properties_8 = details.css("div:nth-child(2) > dl > dd:nth-child(8) ::text").extract()

        properties_9 = details.css("div:nth-child(2) > dl > dt:nth-child(9) ::text").extract_first()        
        properties_10 = details.css("div:nth-child(2) > dl > dd:nth-child(10) ::text").extract()

        properties_11 = details.css("div:nth-child(2) > dl > dt:nth-child(11) ::text").extract_first()
        properties_12 = details.css("div:nth-child(2) > dl > dd:nth-child(12) ::text").extract()
        
        properties_13 = details.css("div:nth-child(2) > dl > dt:nth-child(13) ::text").extract_first()        
        properties_14 = details.css("div:nth-child(2) > dl > dd:nth-child(14) ::text").extract()

        properties_15 = details.css("div:nth-child(2) > dl > dt:nth-child(15) ::text").extract_first()        
        properties_16 = details.css("div:nth-child(2) > dl > dd:nth-child(16) ::text").extract()

        properties_17 = details.css("div:nth-child(2) > dl > dt:nth-child(17) ::text").extract_first()        
        properties_18 = details.css("div:nth-child(2) > dl > dd:nth-child(18) ::text").extract()

        properties_19 = details.css("div:nth-child(2) > dl > dt:nth-child(19) ::text").extract_first()        
        properties_20 = details.css("div:nth-child(2) > dl > dd:nth-child(20) ::text").extract()

        properties_21 = details.css("div:nth-child(2) > dl > dt:nth-child(21) ::text").extract_first()
        properties_22 = details.css("div:nth-child(2) > dl > dd:nth-child(22) ::text").extract()
        
        properties_23 = details.css("div:nth-child(2) > dl > dt:nth-child(23) ::text").extract_first()        
        properties_24 = details.css("div:nth-child(2) > dl > dd:nth-child(24) ::text").extract()

        properties_25 = details.css("div:nth-child(2) > dl > dt:nth-child(25) ::text").extract_first()        
        properties_26 = details.css("div:nth-child(2) > dl > dd:nth-child(26) ::text").extract()

        properties_27 = details.css("div:nth-child(2) > dl > dt:nth-child(27) ::text").extract_first()        
        properties_28 = details.css("div:nth-child(2) > dl > dd:nth-child(28) ::text").extract()

        properties_29 = details.css("div:nth-child(2) > dl > dt:nth-child(29) ::text").extract_first()        
        properties_30 = details.css("div:nth-child(2) > dl > dd:nth-child(30) ::text").extract()

        #drive
        drive_1 = details.css("div:nth-child(3) > dl > dt:nth-child(1) ::text").extract_first()        
        drive_2 = details.css("div:nth-child(3) > dl > dd:nth-child(2) ::text").extract()

        drive_3 = details.css("div:nth-child(3) > dl > dt:nth-child(3) ::text").extract_first()        
        drive_4 = details.css("div:nth-child(3) > dl > dd:nth-child(4) ::text").extract()

        drive_5 = details.css("div:nth-child(3) > dl > dt:nth-child(5) ::text").extract_first()        
        drive_6 = details.css("div:nth-child(3) > dl > dd:nth-child(6) ::text").extract()

        drive_7 = details.css("div:nth-child(3) > dl > dt:nth-child(7) ::text").extract_first()        
        drive_8 = details.css("div:nth-child(3) > dl > dd:nth-child(8) ::text").extract()

        drive_9 = details.css("div:nth-child(3) > dl > dt:nth-child(9) ::text").extract_first()        
        drive_10 = details.css("div:nth-child(3) > dl > dd:nth-child(10) ::text").extract()

        drive_11 = details.css("div:nth-child(3) > dl > dt:nth-child(11) ::text").extract_first()        
        drive_12 = details.css("div:nth-child(3) > dl > dd:nth-child(12) ::text").extract()

        drive_13 = details.css("div:nth-child(3) > dl > dt:nth-child(13) ::text").extract_first()        
        drive_14 = details.css("div:nth-child(3) > dl > dd:nth-child(14) ::text").extract()

        drive_15 = details.css("div:nth-child(3) > dl > dt:nth-child(15) ::text").extract_first()        
        drive_16 = details.css("div:nth-child(3) > dl > dd:nth-child(16) ::text").extract()

        drive_17 = details.css("div:nth-child(3) > dl > dt:nth-child(17) ::text").extract_first()        
        drive_18 = details.css("div:nth-child(3) > dl > dd:nth-child(18) ::text").extract()

        drive_19 = details.css("div:nth-child(3) > dl > dt:nth-child(19) ::text").extract_first()        
        drive_20 = details.css("div:nth-child(3) > dl > dd:nth-child(20) ::text").extract()

        #environment
        environment = Details.css("div.sc-grid-row > div:nth-child(2) > div > div > div")
        
        environment_1 = environment.css("div:nth-child(1) > dl > dt:nth-child(1) ::text").extract_first()
        environment_2 = environment.css("div:nth-child(1) > dl > dd:nth-child(2) ::text").extract()
        
        environment_3 = environment.css("div:nth-child(1) > dl > dt:nth-child(3) ::text").extract_first()
        environment_4a = environment.css("div:nth-child(1) > dl > dd:nth-child(4) > div:nth-child(1) ::text").extract()
        environment_4b = environment.css("div:nth-child(1) > dl > dd:nth-child(4) > div:nth-child(2) ::text").extract()
        environment_4c = environment.css("div:nth-child(1) > dl > dd:nth-child(4) > div:nth-child(3) ::text").extract()
        
        environment_5 = environment.css("div:nth-child(1) > dl > dt:nth-child(5) ::text").extract_first()
        environment_6 = environment.css("div:nth-child(1) > dl > dd:nth-child(6) ::text").extract()
        
        environment_7 = environment.css("div:nth-child(1) > dl > dt:nth-child(7) ::text").extract_first()
        environment_8 = environment.css("div:nth-child(1) > dl > dd:nth-child(8) ::text").extract()
        

        #Equipment
        Equipment = response.css("div.cldt-item[data-item-name='equipments']")
        equipment_1 = Equipment.css("div.sc-grid-row > div:nth-child(1) > h3 ::text").extract_first()
        equipment_2 = Equipment.css("div.sc-grid-row > div:nth-child(1) span::text").extract()
        
        equipment_3 = Equipment.css("div.sc-grid-row > div:nth-child(2) > h3 ::text").extract_first()
        equipment_4 = Equipment.css("div.sc-grid-row > div:nth-child(2) span::text").extract()        
        
        equipment_5 = Equipment.css("div.sc-grid-row > div:nth-child(3) > h3 ::text").extract_first()
        equipment_6 = Equipment.css("div.sc-grid-row > div:nth-child(3) span::text").extract()        
        
        equipment_7 = Equipment.css("div.sc-grid-row > div:nth-child(4) > h3 ::text").extract_first()
        equipment_8 = Equipment.css("div.sc-grid-row > div:nth-child(4) span::text").extract()        
        
        #Description
        Description = response.css("div.cldt-item[data-item-name='description']")
        description = Description.css("div.sc-grid-row > div:nth-child(1) > div:nth-child(1) ::text").extract()
        
        # saving to dictionary
        
        items["make_model"] = make_model
        items["short_description"] = short_description
        items["body_type"] = body_type
        items["price"] = price
        items["vat"] = vat
        items["km"] = km
        items["registration"] = registration
        items["kW"] = kW
        items["hp"] = hp
          
        items[state_1] = state_2
        items[state_3] = state_4
        items[state_5] = state_6
        items[state_7] = state_8
        items[state_9] = state_10
        items[state_11] = state_12
        items[state_13] = state_14
        items[state_15] = state_16
        items[state_17] = state_18
        items[state_19] = state_20
        
        items[properties_1] = properties_2
        items[properties_3] = properties_4
        items[properties_5] = properties_6
        items[properties_7] = properties_8
        items[properties_9] = properties_10
        items[properties_11] = properties_12
        items[properties_13] = properties_14
        items[properties_15] = properties_16
        items[properties_17] = properties_18
        items[properties_19] = properties_20
        items[properties_21] = properties_22
        items[properties_23] = properties_24
        items[properties_25] = properties_26
        items[properties_27] = properties_28
        items[properties_29] = properties_30
        
        items[drive_1] = drive_2
        items[drive_3] = drive_4
        items[drive_5] = drive_6
        items[drive_7] = drive_8
        items[drive_9] = drive_10
        items[drive_11] = drive_12
        items[drive_13] = drive_14
        items[drive_15] = drive_16
        items[drive_17] = drive_18
        items[drive_19] = drive_20
        
        items[environment_1] = environment_2
        items[environment_3] = [environment_4a, environment_4b, environment_4c]
        items[environment_5] = environment_6
        items[environment_7] = environment_8
        
        items[equipment_1] = equipment_2
        items[equipment_3] = equipment_4
        items[equipment_5] = equipment_6
        items[equipment_7] = equipment_8
        
        items["description"] = description
        
        yield items

#! scrapy crawl scout_mmwd
