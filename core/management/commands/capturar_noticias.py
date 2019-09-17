import djclick as click
from scraperNews.spiders.tecmundo import Tecmundo
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

@click.command()
def command():
    runner = CrawlerRunner(get_project_settings())
    d = runner.crawl(Tecmundo)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    click.secho('done!')