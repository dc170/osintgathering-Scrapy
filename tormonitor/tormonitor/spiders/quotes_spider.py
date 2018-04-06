import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://msydqstlz2kzerdg.onion/address/',
    ]

    def parse(self, response):
        for quote in response.css('title'):
            yield {
                'title': quote.css('title::text').extract_first(),
            }

