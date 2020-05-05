# -*- coding: utf-8 -*-


import scrapy
from scrapy.item import Field
from scrapy.loader.processors import MapCompose, TakeFirst


def remove_currency_symbol(text):
    return float(text.strip().replace(' ', '').replace('MYR', '').replace('RM', '').replace('from', ''))


class FoodDeliveryScrapyItem(scrapy.Item):
    restaurant_name = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    restaurant_address = Field(
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
    cuisine_type = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
