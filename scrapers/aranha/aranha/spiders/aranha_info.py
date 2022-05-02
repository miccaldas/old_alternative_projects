import scrapy


class AranhaInfoSpider(scrapy.Spider):
    name = "aranha_info"
    allowed_domains = ["https://tinyurl.com/yjc36yfa"]
    start_urls = ["https://tinyurl.com/yjc36yfa/"]

    def parse(self, response):

        title = response.xpath("//*[@id='habillagepub']/section/header/div/div/h1/text()").extract()
        author = response.xpath("//*[@id='js-authors-trigger']/span/text()").extract()
        date_altered = response.xpath("//*[@id='habillagepub']/section/header/div/section/span/text()").extract()
        content = response.xpath("//*[@id='habillagepub']/section/section[1]/article/p/text()").getall()
        data = zip(title, author, date_altered, content)
        for item in data:
            info = {"title": item[0], "author": item[1], "date_altered": item[2], "content": item[3]}
        yield info
