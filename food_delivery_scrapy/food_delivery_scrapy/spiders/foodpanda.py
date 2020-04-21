import requests
import scrapy


class FoodPandaSpider(scrapy.Spider):
    name = "foodpanda"
    start_urls = []

    # Foodpanda API
    base_url = f"https://discovery.deliveryhero.io/pandora/api/v5/vendors?cuisine=&food_characteristic=&budgets=&has_free_delivery=1&search_term=&latitude=5.3441567&longitude=100.311548&include=characteristics%2Cmetadata%2Cdiscounts&new_sorting=true&language_id=1&vertical=restaurants&configuration=Variant1&country=my&customer_id=2324140&customer_hash=9df193e2adcbc4d350a1fb3bcdd151b2"
    response = requests.get(base_url)
    restaurant_urls = response.json()['data']['items']

    for url in restaurant_urls:
        start_urls.append(url['redirection_url'])

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
