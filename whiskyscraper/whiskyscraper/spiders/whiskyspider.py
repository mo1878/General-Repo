import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'scrapes'
    #page_number = 2 
    #start_urls = ['https://www.whiskyshop.com/world-whiskies/all?p=1']

    start_urls = []

    def __init__(self):

        url = 'https://www.whiskyshop.com/world-whiskies/all?p='

        for page in range(1,5):
            self.start_urls.append(url + str(page))

    def parse(self, response):

        for response in response.css('div.product-item-info'):
            yield {
                'name': response.css('a.product-item-link::text').get(),
                'price': response.css('span.price::text').get(),
                'link': response.css('a.product-item-link').attrib['href'],
            }

        # next_page = 'https://www.whiskyshop.com/world-whiskies/all?p=2' + str(WhiskySpider.page_number)
        # if WhiskySpider.page_number <= 6:
        #     WhiskySpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)
