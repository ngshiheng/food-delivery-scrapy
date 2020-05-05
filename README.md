<h1 align="center"><strong>Food Delivery Scrapy</strong></h1>

<br />

<div align="center"><img src="https://i.imgur.com/lrx4RuF.png" /></div>

<br />

- Scrape the restaurant name, url, dish name and price of each of the item on the menu listed on Foodpanda & DeliverEat for a given location, visualize them using [metabase](https://www.metabase.com/)
- Please read this [article](https://benbernardblog.com/web-scraping-and-crawling-are-perfectly-legal-right/) before using this
- See example `JSON` output [here](https://github.com/ngshiheng/food-delivery-scrapy/tree/master/food_delivery_scrapy/food_delivery_scrapy/example_output)

## Setup

- Python 3.6+
- Install all the dependencies using [pipenv](https://pipenv.pypa.io/en/latest/)
- Download & install [splash](https://splash.readthedocs.io/en/stable/install.html#linux-docker) on your machine, this is used to scrape dynamic contents

## Usage

Scraping the entire restaurants is going to take some time, for tryout/debug/development, add `DEBUG=True` to your command, e.g.:

```
# JSON output
DEBUG=True scrapy crawl foodpanda -o food_delivery_scrapy/output/foodpanda.json

# SQL output
DEBUG=True scrapy crawl foodpanda
```

Set `PROXY_POOL_ENABLED = True` at `settings.py` to use proxy pool

### JSON output

#### Foodpanda

```sh
scrapy crawl foodpanda -o food_delivery_scrapy/output/foodpanda.json
```

#### DeliverEat

```sh
# Get the URLs of all the available restaurants
scrapy crawl get_delivereat_restaurants

# Get the final data
scrapy crawl delivereat -o food_delivery_scrapy/output/delivereat.json
```

### Save to PostgreSQL

- Make sure your `postgresql` is running
- `createdb food_delivery_scrapy`
- Make sure `splash` is running

```sh
scrapy crawl get_delivereat_restaurants # You only need to run this once
scrapy crawl delivereat
scrapy crawl foodpanda
```
