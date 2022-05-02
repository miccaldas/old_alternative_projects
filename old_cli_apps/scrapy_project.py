"""This will automate the creation of Scrapy projects."""

import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])

spiders = "/home/mic/python/cli_apps/cli_apps/spider_folders/"


class ScrapyProject:
    """In this class will be represented the steps needed to setup
    a Scrapy project. Each method will be a task."""

    def __init__(self, project_name, spider_name, domain_name):
        self.project_name = project_name
        self.spider_name = spider_name
        self.domain_name = domain_name

    @logger.catch
    @snoop
    def project_creation(self):
        """Where will create a scrapy project in location and
        name to be defined."""

        cmd = f"scrapy startproject {self.project_name}"
        subprocess.run(cmd, shell=True)

    @logger.catch
    @snoop
    def settings_definition(self):
        """
        We wll deal with all the usual changes on
        the settings.
        """

        with open(f"{spiders}{self.project_name}/{self.project_name}/settings.py", "a") as d:
            d.write('FEED_EXPORT_FIELDS = ["presentation"]')
            d.write("\n")
            d.write('FEED_FORMAT = "csv"')
            d.write("\n")
            d.write('FEED_URI = "results.csv"')

    @logger.catch
    @snoop
    def spider(self):
        """Creation of the file that defines the spider."""

        class_name = f"{self.spider_name[:-3]}".capitalize()  # Capitalizes only the first character in string.
        with open(f"{spiders}{self.project_name}/{self.project_name}/spiders/{self.spider_name}", "w") as f:
            f.write("import scrapy   # noqa: F401\n")
            f.write("import snoop\n")
            f.write("import isort   # noqa: F401\n")
            f.write("from itertools import zip_longest")
            f.write("\n\n\n")
            f.write(f"class {class_name}(scrapy.Spider):\n")
            f.write(f"    name = '{self.spider_name[:-3]}'\n")
            f.write(f"    start_urls = ['{self.domain_name}']\n")
            f.write("\n")
            f.write("    @snoop\n")
            f.write("    def parse(self, response):\n")
            f.write("""        srch_descriptions = response.xpath('//*[@id="description"]/div/p/text()').getall()""")
            f.write("\n")
            f.write("        results = {'description': srch_descriptions}\n")
            f.write("        print(results)\n")
            f.write("        with open('results.txt', 'a') as f:\n")
            f.write("""           f.write(f"{results}")\n""")
            f.write("\n")
            f.write("        return results\n")


if __name__ == "__main__":
    (ScrapyProject)
