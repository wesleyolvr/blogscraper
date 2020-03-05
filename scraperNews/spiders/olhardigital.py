import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor


class OlharDigital(scrapy.Spider):
    name= "Olhar digital"
    start_urls = ['https://olhardigital.com.br/noticias/']

    def parse(self,response):
        item = {}
        noticias = response.xpath('//div[@class="blk-items"]')
        imagens = noticias.xpath('//div[@class="ite-img"]/img/@data-src').extract()
        titulos_noticias = noticias.xpath('//h3[@class="ite-nfo nfo-tit"]/text()').extract()
        for titulo, imagem in zip(titulos_noticias,imagens):
            item['Title_new'] = titulo
            imagem = "https:"+imagem
            item['Picture'] = imagem
            yield item