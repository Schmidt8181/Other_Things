# -*- coding: utf-8 -*-
import scrapy


class ConiferSpider(scrapy.Spider):
    name = 'Conifer'
    allowed_domains = ['www.greatplantpicks.org']
    start_urls = ['http://www.greatplantpicks.org/plantlists/by_plant_type/conifer',
    'http://www.greatplantpicks.org/plantlists/by_plant_type/tree', 'http://www.greatplantpicks.org/plantlists/by_plant_type/perennial']


    #def parse(self, response):
    #    filename = response.url.split("/")[-2] + '.html'
    #    with open(filename, 'wb') as f:
    #        f.write(response.body)


    def parse(self, response):
        for sel in response.xpath('//tbody/tr'):
            item = ConifersItem()
            item['height'] = sel.xpath('td[@class="height"]/text()').extract()
            item['genus'] = sel.xpath('td[@class="plantname"]/a/span[@class="genus"]/text()').extract()
            item['type'] = sel.xpath('td[@class="type"]/text()').extract()
            yield item

class ConifersItem(scrapy.Item):
    genus = scrapy.Field()
    height = scrapy.Field()
    type = scrapy.Field()
    pass
