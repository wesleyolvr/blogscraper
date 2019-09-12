import scrapy
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

class Tecmundo(scrapy.Spider):
    name= "Tecmundo"
    start_urls = ['https://www.tecmundo.com.br/']

    def parse(self,response):
        item = {}
        news = response.xpath("//h3[@class='tec--card__title']/a/text()").extract()
        for new in news:
            item['Title_new'] = new
            yield item


runner = CrawlerRunner(get_project_settings())
d = runner.crawl(Tecmundo)
d.addBoth(lambda _: reactor.stop())
reactor.run()
