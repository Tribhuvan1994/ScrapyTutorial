import scrapy

class HondaSpider(scrapy.Spider):
    name = "hondas"
    start_urls = [
        https://honda.com.np/motorcycles/
    ]
    
    def parse(self, response):
        
        # items = TutorialItem()
        
        all_div_quotes = response.css('div.row') #get the data of quote under div element with quote class
        print(all_div_quotes)
        # for quotes in all_div_quotes:
        #     title = quotes.css('span.text::text').extract() #extract data of span with text class
        #     author = quotes.css('.author::text').extract() #extract data of author class
        #     tag = quotes.css('.tag::text').extract() #extract data of tag class
            
        #     items['title'] = title
        #     items['author'] = author
        #     items['tag'] = tag
            
        #     yield items
        
        # next_page = response.css('li.next a::attr(href)').get()
        
        # if next_page is not None:
        #     yield response.follow(next_page, callback= self.parse)