import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from random import randint


class Tecmundo(scrapy.Spider):
    name= "Tecmundo"
    start_urls = ['https://www.tecmundo.com.br/']

    def parse(self,response):
        item = {}
        noticias = response.xpath('//figure[@class="tec--card__thumb"]//img')
        for new in noticias:
            item['Title_new'] = new.xpath('@alt').extract_first().replace('Imagem de: ','')
            item['Picture'] = new.xpath('@data-src').extract_first()
            yield item
            
    
            
        

        
