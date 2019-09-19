import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor


class OlharDigital(scrapy.Spider):
    name= "Olhar digital"
    start_urls = ['https://olhardigital.com.br/']

    def parse(self,response):
        item = {}
        news = response.xpath('//div[@class="blk-items"]//h3[@class="ite-nfo nfo-tit"]//text()').extract()
        for new in news:
            item['Title_new'] = new
            yield item