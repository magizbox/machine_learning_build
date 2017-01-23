import scrapy

class CategorySpider(scrapy.Spider):
    name = 'tkaraokespider'
    start_urls = ['http://poem.tkaraoke.com/tim.tho?q=t%E1%BA%A3n-%C4%91%C3%A0&t=6']

    def parse(self, response):
        for title in response.css("table.SResult tr"):
            yield {'title': title.css("::text").extract_first()}

        next_doms = response.css("a.a-name-poem")
        for next_dom in next_doms:
            url = next_dom.css("::attr(href)").extract_first()
            yield scrapy.Request(response.urljoin(url), callback=self.poem_parse)

    def poem_parse(self, response):
        pass
