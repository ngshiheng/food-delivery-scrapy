# Food Delivery Scrapy

- Scrape the restaurant name, url & prices of each of the item on the menu listed on Foodpanda & DeliverEat
- Please read this [article](https://benbernardblog.com/web-scraping-and-crawling-are-perfectly-legal-right/) before using this

## Setup

Install the dependencies using `pipenv`

## Usage

### Foodpanda

```sh
scrapy crawl foodpanda -o food_delivery_scrapy/output/foodpanda.json
```

### DeliverEat

```sh
# Get the URLs of all the available restaurants
scrapy crawl delivereat_restaurants

# Get the final data
scrapy crawl delivereat -o food_delivery_scrapy/output/delivereat.json
```
