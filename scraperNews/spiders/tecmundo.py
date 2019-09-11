import scrapy

class Tecmundo(scrapy.Spider):
    name= Tecmundo
    start_urls = ['https://www.tecmundo.com.br/']

    def parse(self,response):
        item = {}
        news = response.xpath("//h3[@class='tec--card__title']/a/text()").extract()
        for new in news:
            item['Title_new'] = new
            yield new
