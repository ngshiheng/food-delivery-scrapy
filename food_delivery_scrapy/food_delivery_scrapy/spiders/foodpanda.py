from food_delivery_scrapy.items import FoodDeliveryScrapyItem
from scrapy.loader import ItemLoader
import scrapy
import requests
from food_delivery_scrapy.config import FOODPANDA_API_ENDPOINT, DEBUG, FOODPANDA_EXAMPLE_URLS


class FoodPandaSpider(scrapy.Spider):
    """
    - Query all the restaraunt URLs through Foodpanda's API
    - Get data from all restaurants
    """
    name = "foodpanda"
    if DEBUG:
        start_urls = FOODPANDA_EXAMPLE_URLS
    else:
        BASE_URL = FOODPANDA_API_ENDPOINT
        response = requests.get(BASE_URL)
        restaurant_urls = response.json()['data']['items']
        start_urls = [url['redirection_url'] for url in restaurant_urls]

    def parse(self, response):
        restaurant_name = response.css('.vendor-info-main-headline.item h1.fn::text').get()
        restaurant_address = response.css('.vendor-location::text').get()
        cuisine_types = response.css('.vendor-info-main-details-cuisines li::text').getall()

        # Filter out cuisine type with length more than 10 & remove duplicates from the list
        cuisine_types = list(dict.fromkeys(filter(lambda cuisine: len(cuisine) <= 10, cuisine_types)))
        cuisine_type = ','.join(cuisine_types)

        dishes = response.css('.item-react-root')
        for dish in dishes:
            loader = ItemLoader(item=FoodDeliveryScrapyItem(), selector=dish)
            loader.add_value('restaurant_name', restaurant_name)
            loader.add_value('restaurant_address', restaurant_address)
            loader.add_value('cuisine_type', cuisine_type)
            loader.add_css('dish_name', 'span::text')
            loader.add_css('dish_price', '.price.p-price::text')
            loader.add_value('url', response.request.url)
            yield loader.load_item()
