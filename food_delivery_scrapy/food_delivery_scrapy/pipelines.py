from sqlalchemy.orm import sessionmaker
from food_delivery_scrapy.models import Restaurant, Dish, db_connect, create_table


class FoodDeliveryScrapyPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Save dishes in the database
        This method is called for every item pipeline component
        """
        session = self.Session()
        restaurant = Restaurant()
        dish = Dish()

        restaurant.restaurant_name = item['restaurant_name']
        restaurant.url = item['url']
        dish.dish_name = item['dish_name']
        dish.dish_price = item['dish_price']

        exist_restaurant = session.query(Restaurant).filter_by(restaurant_name=restaurant.restaurant_name).first()
        if exist_restaurant is not None:
            dish.restaurant = exist_restaurant
        else:
            dish.restaurant = restaurant

        try:
            session.add(dish)
            session.commit()

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()

        return item
