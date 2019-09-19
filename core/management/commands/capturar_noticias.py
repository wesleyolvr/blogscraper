import djclick as click
from scraperNews.spiders.tecmundo import Tecmundo
from scraperNews.spiders.olhardigital import OlharDigital
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner,CrawlerProcess
from twisted.internet import reactor
from scrapy.utils.log import configure_logging

@click.command()
def command():
    process = CrawlerProcess(get_project_settings())
    process.crawl(Tecmundo)
    process.crawl(OlharDigital)
    process.start()