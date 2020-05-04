import scrapy
from scrapy_splash import SplashRequest
from scrapy.loader import ItemLoader
from food_delivery_scrapy.items import FoodDeliveryScrapyItem


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
        restaurant_name = response.css("p.fs-m.my-0::text").get()
        dishes = response.css('div.card-stacked')
        for dish in dishes:
            loader = ItemLoader(item=FoodDeliveryScrapyItem(), selector=dish)
            loader.add_value('restaurant_name', restaurant_name)
            loader.add_css('dish_name', 'h1::text')
            loader.add_css('dish_price', 'b::text')
            loader.add_value('url', response.request._original_url)
            yield loader.load_item()
