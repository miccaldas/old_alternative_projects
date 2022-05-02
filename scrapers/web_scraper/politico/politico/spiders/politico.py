import scrapy


class PoliticoSpider(scrapy.Spider):
    name = "politico"
    allowed_domains = ["politico.eu"]
    start_urls = [
        "https://www.politico.eu/article/italy-green-pass-bar-museum-restaurant-coronavirus-vaccine-appointments//"
    ]

    def parse(self, response):
        title = response.xpath("/html/body/main/div/div[2]/div/div/div/div/div/div/h1/text()").extract()
        author = response.xpath(
            "/html/body/main/div/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[2]/a/text()"
        ).extract()
        date_altered = response.xpath(
            "/html/body/main/div/div[3]/div/div[1]/div[1]/div[2]/div/div/div/div[3]/span[1]/text()"
        ).extract()
        content = response.xpath("/html/body/main/div/div[3]/div/div[1]/div[3]/p/text()").getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {
                "title": item[0],
                "author": item[1],
                "date_altered": item[2],
                "content": item[3],
            }
        yield info
