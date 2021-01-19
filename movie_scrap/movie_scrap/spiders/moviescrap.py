# import scrapy
# from myscaper.items import MyscaperItem
# from scrapy.http import Request


# URL = 'https://movie.naver.com/movie/point/af/list.nhn&page=%s'
# startpage=1


# class MoviescrapSpider(scrapy.Spider):
#     name = 'moviescrap'
#     allowed_domains = ['naver.com']
#     start_urls = [URL%startpage]

#     def start_requests(self):
#         for i in range(3):
#             yield Request(url=URL %(i +startpage),callback=self.parse)

#     def parse(self,response):
#         titles = response.xpath('//*[@id="old_content"]/table/tbody/tr[1]/td[2]/a[1]').extract()
#         writers = response.css('.author::text').extract()
#         previews = response.css('.list_netizen_score::text').extract()
#         grades = response.css('st_on::text').extract()
#         dates = response.css('.num::text').extract()

#         items =[]

#         for idx in range(len(titles)):
#             item = MyscaperItem()
#             item['title'] = titles[idx]
#             item['writer'] = writers[idx]
#             item['preview'] = previews[idx]
#             item['grade'] = grades[idx]
#             item['date'] = dates[idx]


#             items.append(item)

#         return items

import scrapy
from myscaper.items import MyscaperItem
from scrapy.http import Request

URL = 'http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258&page=%s'
start_page = 1

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = [URL % start_page]
    
    def start_requests(self):
        '''
        http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258&page=1
        http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258&page=2
        '''
        for i in range(2): # 0, 1 ~ 9 -> 1 ~ 10
            yield Request(url=URL % (i + start_page), callback=self.parse)

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        
        # zip(titles, writers, previews)
        items = []
        # items에 XPATH, CSS를 통해 추출한 데이터를 저장 
        for idx in range(len(titles)):
            item = MyscaperItem()
            item['title'] = titles[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)

        return items



