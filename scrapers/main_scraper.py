"""Main module of the app. Where all functionalities are accessed from"""
import scrapy
from scraper import Scraper
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("spam.log", level="DEBUG", format=fmt)
logger.add("error.log", level="ERROR", format=fmt)


def main():
    """Here we start, sequentially, all the steps needed to create a scraping campaign."""
    rasoura = Scraper(
        "guardian",
        "guardian_newspaper",
        "theguardian.com" "/home/mic/python/old_alternative_projects",
        "https://tinyurl.com/ygwo39yd",
        "/html/body/article/div/div/div[4]/div/div/h1/text())",
        "/html/body/article/div/div/div[8]/div/div/div/div[1]/div/address/div/a[1]/text()",
        "/html/body/article/div/div/div[8]/div/div/div/div[1]/div/div/div/label/text()",
        "//*[@id='maincontent']/div/p/text())",
    )

    # rasoura.dislocation()
    # rasoura.start_project()
    # rasoura.start_spider()
    # rasoura.edit_spider_file_clean_file()
    # rasoura.edit_spider_file_parse_function()
    # rasoura.dislocation1()
    # rasoura.settings()
    # rasoura.dislocation2()
    rasoura.crawl()
    rasoura.result()


main()
