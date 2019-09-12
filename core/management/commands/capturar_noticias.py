import djclick as click
from scraperNews.spiders.tecmundo import Tecmundo,runner

@click.command()
def command():
    process = runner.crawl(Tecmundo)
    click.secho('done!')