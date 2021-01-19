import scrapy
from movie_scrap.items import MovieScrapItem
from scrapy.http import Request



URL = 'https://movie.naver.com/movie/point/af/list.nhn?&page=%s'
startpage=1


class MoviescrapSpider(scrapy.Spider):
    name = 'moviescrap'
    allowed_domains = ['naver.com']
    start_urls = [URL%startpage]

    def start_requests(self):
        for i in range(3):
            yield Request(url=URL %(i +startpage),callback=self.parse)

    def parse(self,response):
        titles = response.xpath('//*[@id="old_content"]/table/tbody/tr/td[2]/a[1]/text()').extract()
        authors = response.css('.author::text').extract()
        reports = response.css('.title *::text').extract()
        # grades = response.css('st_on::text').extract()
        dates = response.css('.num::text').extract()

        items =[]

        for idx in range(len(titles)):
            item = MovieScrapItem()
            item['title'] = titles[idx]
            item['author'] = authors[idx]
            item['report'] = reports[idx]
            # item['grade'] = grades[idx]
            item['date'] = dates[idx]


            items.append(item)

        return items


