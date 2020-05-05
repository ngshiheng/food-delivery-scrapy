import datetime
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, DateTime, Float
from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True)
    restaurant_name = Column('restaurant_name', String(255))
    restaurant_address = Column('restaurant_address', String(255))
    cuisine_type = Column('cuisine_type', String(255))
    url = Column('url', String)
    dishes = relationship('Dish', backref='restaurant')
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    time_updated = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.now())


class Dish(Base):
    __tablename__ = "dish"

    id = Column(Integer, primary_key=True)
    dish_name = Column('dish_name', String)
    dish_price = Column('dish_price', Float)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    time_updated = Column(DateTime(timezone=True), default=datetime.datetime.utcnow, onupdate=func.now())
