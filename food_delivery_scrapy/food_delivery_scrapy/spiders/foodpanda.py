import requests
import scrapy
from scrapy.loader import ItemLoader
from food_delivery_scrapy.items import FoodDeliveryScrapyItem


class FoodPandaSpider(scrapy.Spider):
    """
    - Query all the restaraunt URLs through Foodpanda's API
    - Get data from all restaurants
    """
    name = "foodpanda"

    # Foodpanda API
    BASE_URL = f"https://discovery.deliveryhero.io/pandora/api/v5/vendors?cuisine=&food_characteristic=&budgets=&has_free_delivery=1&search_term=&latitude=5.3441567&longitude=100.311548&include=characteristics%2Cmetadata%2Cdiscounts&new_sorting=true&language_id=1&vertical=restaurants&configuration=Variant1&country=my&customer_id=2324140&customer_hash=9df193e2adcbc4d350a1fb3bcdd151b2"
    response = requests.get(BASE_URL)
    restaurant_urls = response.json()['data']['items']
    start_urls = [url['redirection_url'] for url in restaurant_urls]

    def parse(self, response):
        restaurant_name = response.css('.vendor-info-main-headline.item h1.fn::text').get()
        dishes = response.css('.item-react-root')
        for dish in dishes:
            loader = ItemLoader(item=FoodDeliveryScrapyItem(), selector=dish)
            loader.add_value('restaurant_name', restaurant_name)
            loader.add_css('dish_name', 'span::text')
            loader.add_css('dish_price', '.price.p-price::text')
            loader.add_value('url', response.request.url)
            yield loader.load_item()
