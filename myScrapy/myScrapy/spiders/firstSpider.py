import scrapy


class FirstspiderSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['https://www.politico.com/search?q=technology/']
    start_urls = ['https://www.politico.com/search?q=technology/']

    def parse(self, response):
        pass


