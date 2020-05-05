import os

DEBUG = os.getenv("DEBUG", False) in ["true", "True"]
DB_NAME = "food_delivery_scrapy"
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
FOODPANDA_API_ENDPOINT = os.getenv("FOODPANDA_API_ENDPOINT")

FOODPANDA_EXAMPLE_URLS = ['https://www.foodpanda.my/restaurant/r0ff/starbucks-borders-queensbay-mall-2',
                          'https://www.foodpanda.my/restaurant/n8jp/kfc-queensbay-mall',
                          'https://www.foodpanda.my/restaurant/o1as/cube-coffee-one-precinct']


DELIVEREAT_EXAMPLE_URLS = [
    'https://jom.delivereat.my/PG54/restaurants/9653',
    'https://jom.delivereat.my/PG54/restaurants/9631',
    'https://jom.delivereat.my/PG54/restaurants/9291'
]
