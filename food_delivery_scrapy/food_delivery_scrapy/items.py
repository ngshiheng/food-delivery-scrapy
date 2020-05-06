# -*- coding: utf-8 -*-


import scrapy
from scrapy.item import Field
from scrapy.loader.processors import MapCompose, TakeFirst
from re import sub
from decimal import Decimal


def convert_money(money):
    return Decimal(sub('[^0-9.]', '', money))


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
        input_processor=MapCompose(convert_money),
        output_processor=TakeFirst()
    )
    cuisine_type = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
