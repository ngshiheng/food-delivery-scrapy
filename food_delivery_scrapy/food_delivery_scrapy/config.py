import os

DEBUG = os.getenv("DEBUG", False) in ["true", "True"]
DB_NAME = "food_delivery_scrapy"
PGUSER = os.getenv("PGUSER")
PGPASSWORD = os.getenv("PGPASSWORD")
FOODPANDA_API_ENDPOINT = os.getenv("FOODPANDA_API_ENDPOINT")
