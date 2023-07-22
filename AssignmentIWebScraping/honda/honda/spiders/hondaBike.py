import scrapy
from ..items import HondaItem

class HondabikeSpider(scrapy.Spider):
    name = "hondaBike"
    start_urls = ["https://honda.com.np/motorcycles"]

    def parse(self, response):
        items = HondaItem()
        
        bikeName = response.css('p::text').extract()
        
        items['bikeName'] = bikeName
        
        yield items