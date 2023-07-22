import scrapy
import requests 
from bs4 import BeautifulSoup

class MerolaganiSpider(scrapy.Spider):
    name="lagani"
    start_urls = ["https://merolagani.com/MarketSummary.aspx?type=turnovers"]
    
    def parse(self, response):
        
        #items = MerolaganiItem()
        
        footer_data = response.css('div.footer')
        
        for data in footer_data:
            tags = data.css('div').extract()
            
            #items['tags'] = tags
            
            yield tags