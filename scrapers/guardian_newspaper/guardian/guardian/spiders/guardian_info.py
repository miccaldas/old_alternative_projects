import scrapy


class GuardianInfoSpider(scrapy.Spider):
    name = "guardian_info"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/world/2021/aug/08/taliban-seize-symbolic-victory-with-capture-of-kunduz"]

    def parse(self, response):

        title = response.xpath("/html/body/article/div/div/div[4]/div/div/h1/text()").extract()
        author = response.xpath(
            "/html/body/article/div/div/div[8]/div/div/div/div[1]/div/address/div/a[1]/text()"
        ).extract()
        date_altered = response.xpath(
            "/html/body/article/div/div/div[8]/div/div/div/div[1]/div/div/div/label/text()"
        ).extract()
        content = response.xpath("//*[@id='maincontent']/div/p/text()").getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {"title": item[0], "author": item[1], "date_altered": item[2], "content": item[3]}
            yield info
