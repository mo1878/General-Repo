import scrapy 

class AsosSpider(scrapy.Spider):
    name = 'asoslol'

    def __init__(self):

        for page in range(1,20):
            url = f'https://www.asos.com/us/search/?currentpricerange=10-215&page={page}&q=cargo%20pants%20men&refine=attribute_1046:8430'
            self.start_urls.append(url + {page})


            start_urls = []
            urls = [url]




    def parse(self, response):

        for response in response.css('article.product-202686055'):
            yield {
                'Item_Name': response.css('a.aria-label').get(),
                'Item_Price': response.css('span._16nzq18::text').get(),
            }
