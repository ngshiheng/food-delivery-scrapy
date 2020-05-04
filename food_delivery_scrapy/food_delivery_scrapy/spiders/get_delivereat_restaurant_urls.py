import os
import scrapy
from scrapy_splash import SplashRequest


class DeliverEatSpider(scrapy.Spider):
    """
    Get the URLs of all the restaurant and save it into a txt file
    URLs to be consumed by delivereat.py spider
    """
    name = "get_delivereat_restaurants"
    start_urls = ['https://jom.delivereat.my/PG54/restaurants']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        ALL_RESTAURANT_CONTAINER_SELECTOR = '.row.mt-5'
        all_restaurants = response.css(ALL_RESTAURANT_CONTAINER_SELECTOR)

        RESTAURANT_INFO_SELECTOR = 'div.card'
        restaurants = all_restaurants.css(RESTAURANT_INFO_SELECTOR)

        output_path = os.path.join(os.getcwd(), 'food_delivery_scrapy', 'output', 'restaurant_list.txt')
        with open(output_path, 'w') as f:
            for restaurant in restaurants:
                url = f"https://jom.delivereat.my{restaurant.css('a::attr(href)').get()}"
                f.write(url)
                f.write("\n")
