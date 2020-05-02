import scrapy
from scrapy_splash import SplashRequest


class DeliverEatSpider(scrapy.Spider):
    name = "delivereat"
    start_urls = ['https://jom.delivereat.my/PG54/restaurants']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):

        RESTAURANT_INFO_SELECTOR = 'div.card-content'
        restaurants = response.css(RESTAURANT_INFO_SELECTOR)
        for restaurant in restaurants:
            url = restaurant.css('a::attr(href)').get()

            yield {
                'restaurant_name': restaurant.css('.res-name::text').get(),
                'url': f"https://jom.delivereat.my{url}",
            }
