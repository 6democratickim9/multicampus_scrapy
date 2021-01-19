

import scrapy


class MovieScrapItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    report = scrapy.Field()
    # grade = scrapy.Field()
    date = scrapy.Field()

