import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ["https://www.amazon.com/s?k=books+last+30+days&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&ds=v1%3A7TaXtE602dnjzmnZYQIqnLwBL9LwC6fCmc335POOHDk&crid=X8Z1MQ9ESUFK&qid=1690035366&rnid=1250225011&sprefix=books+last+30+day%2Caps%2C319&ref=sr_nr_p_n_publication_date_1"]

    def parse(self, response):
        items = AmazonItem()
        
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base , .a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        
        items['product_name'] = product_name
        items['product_author'] = product_author
        
        yield items
