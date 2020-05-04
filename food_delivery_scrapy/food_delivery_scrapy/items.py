# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime



def remove_currency_symbol(text):
    return float(text.strip().replace(' ', '').replace('MYR', '').replace('RM', '').replace('from', ''))


class FoodDeliveryScrapyItem(scrapy.Item):
    restaurant_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    url = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    dish_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    dish_price = Field(
        input_processor=MapCompose(remove_currency_symbol),
        output_processor=TakeFirst()
    )
