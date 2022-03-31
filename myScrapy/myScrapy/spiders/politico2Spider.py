import scrapy
import json
from scrapy.http import Request


class Politico2spiderSpider(scrapy.Spider):
    name = 'politico2Spider'
    allowed_domains = ['https://www.politico.com/']
    start_urls = []

    with open("moreArticles.json") as f:
        data = json.load(f)
        for i in data:
            temp = i['Link']
            start_urls.append(str(temp))

    def parse(self, response):
        wrapper = response.css('article.content')
        yield {
            'Title':wrapper.css('h1::text').get(),
            'Text':wrapper.css('p::text').getall()
        }


