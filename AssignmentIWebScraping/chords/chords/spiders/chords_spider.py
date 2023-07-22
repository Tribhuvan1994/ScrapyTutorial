from pathlib import Path

import scrapy

class ChordsSpider(scrapy.Spider):
    name = "chords"
    start_urls = [
            "https://lyricalchord.com/maya-ko-bhasa-lyrics-chords/",
    ]
    
    def parse(self, response):
        all_div_lines = response.css('div.entry') #get the data of quote under div element with quote class
        
        for lines in all_div_lines:
            text = lines.css('p::text').extract()
            span = lines.css('span::text').extract()
            yield{
                'text': text,
                'span': span
            }