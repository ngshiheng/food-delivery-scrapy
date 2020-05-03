import scrapy
from scrapy_splash import SplashRequest


class DeliverEatSpider(scrapy.Spider):
    """
    - Read restaurant URL from restaurant_list.txt which was scrapped with get_delivereat_restaurants spider
    - Get data from all restaurants
    """
    name = "delivereat"
    with open('food_delivery_scrapy/output/restaurant_list.txt', 'r') as f:
        restaurant_urls = f.readlines()
    start_urls = [url.strip() for url in restaurant_urls]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        dish_info = {}
        RESTAURANT_INFO_SELECTOR = 'p.fs-m.my-0::text'
        DISH_SELECTOR = 'div.card-stacked'
        dishes = response.css(DISH_SELECTOR)

        for dish in dishes:
            dish_name = dish.css('h1::text').get().strip().replace('  ', '')
            dish_price = dish.css('b::text').get().strip().replace('RM', '')
            dish_info[dish_name] = float(dish_price)

        yield {
            'restaurant_name': response.css(RESTAURANT_INFO_SELECTOR).get().strip(),
            'url': response.request._original_url,
            'menu': dish_info
        }
