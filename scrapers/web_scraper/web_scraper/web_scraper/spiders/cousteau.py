import scrapy


class CousteauSpider(scrapy.Spider):
    name = "cousteau"
    allowed_domains = ["www.dn.pt"]
    start_urls = ["https://www.dn.pt/cultura/celine-cousteau-nao-sou-a-unica-herdeira-do-meu-avo-11051058.html/"]

    def parse(self, response):
        yield {"p": response.xpath("//html/body/main/article/div/div/div/div/div[2]/p/text()").extract()}
