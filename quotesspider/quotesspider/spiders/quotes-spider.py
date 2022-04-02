import scrapy

"""
A simple scrapy spidet to crawl quotes and author name from
https://quotes.toscrape.com/ site

how to run the spider

scrapy runspider first-spider.py -o quotes.json

"""


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # spider name
    # the url to crawl
    start_urls = [
        'https://quotes.toscrape.com/',
    ]

    def parse(self, response):
        quotes_block = response.xpath('//div[@class="quote"]')  # get the div block of each quote
        for quote in quotes_block:
            yield {
                'quote': quote.xpath('span/text()').get(),  # xpath to get quotes
                'author': quote.xpath('span/small/text()').get()  # xpath to get the author

            }

        next_page_link = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page_link is not None:
            next_page = response.urljoin(next_page_link)
            yield scrapy.Request(next_page, callback=self.parse)
