import scrapy

class PoliticoSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['politico.com']
    start_urls = ['https://www.politico.com/search?q=technology/']

    def parse(self, response):
        print("This is the response Yooooo",response)
        for articles in response.css('article.story-frag.format-ml'):
            yield {
                "Title" : articles.css('img').attrib['alt'],
                "Link" : articles.css('a').attrib['href'],
                "Intro" : articles.css('div.tease').css('p::text').get(),
                "Category": articles.css('p.category::text').get(),
                "DateAndTime": articles.css('time').attrib['datetime'],
            }

        for button in response.css("button"):
            if button.css('::text').get() == "Next page »":
                next_page = button.attrib['href']
                print(" \n Next Page : "+ next_page + "\n")
                yield response.follow(next_page,callback=self.parse)




