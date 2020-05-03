import requests
import scrapy


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
        dish_info = {}
        RESTAURANT_INFO_SELECTOR = '.vendor-info-main-headline.item h1.fn::text'
        DISH_SELECTOR = '.item-react-root'
        dishes = response.css(DISH_SELECTOR)
        for dish in dishes:
            dish_name = dish.css('span::text').get().strip().replace('  ', '')
            dish_price = dish.css('.price.p-price::text').get().strip().replace('  ', '').replace('MYR', '').replace('from', '')
            dish_info[dish_name] = float(dish_price)

        yield {
            'restaurant_name': response.css(RESTAURANT_INFO_SELECTOR).get().strip(),
            'url': response.request.url,
            'menu': dish_info
        }
