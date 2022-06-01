import scrapy
from scrapy import Request

class UHomeSpider(scrapy.Spider):
    name = 'scraper'

    start_urls = []
    urls = ['https://en.uhomes.com/uk/rent']

    def __init__(self):

        url = 'https://en.uhomes.com/uk/rent'

        for page in range(1, 25):
            self.start_urls.append(url + '/' + 'pga' + str(page))

    def parse(self, response):
  

        for response in response.css('div.house-box'):

            if response.css('p.comment.icon::text').get() is None and response.css('em::text').get() is None:
                print('No Rating and No Count Rating')
            # elif response.css('em::text').get() is None:
            #     print('No Count of Rating')
            #     pass
            else: 
                yield {
                    'accom_name': response.css('a.name::text').get(),
                    'accom_rating': response.css('p.comment.icon::text').get(),
                    'num_rating': response.css('em::text').get().replace('(', '').replace(')', ''),
                }

            
                
