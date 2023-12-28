from countries.country_provider import CountryProvider
from web_crawler.crawler import MichelinCrawler
from web_crawler.restaurant import RESTAURANT_FIELD_NAMES
from pathlib import Path

import csv

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--country', required=True, dest='country_name', type=str, help='The name of the country to fetch')
args = parser.parse_args()

country = CountryProvider().get_country(args.country_name)
crawler = MichelinCrawler(country)
crawler.fetch_pages()
crawler.fetch_cards()
restaurants = crawler.get_restaurant_objects()

Path("./results").mkdir(exist_ok=True)
with open(f"./results/{country.shortcode}.csv", "w", newline="", encoding="utf-8") as csvfile:
	print(RESTAURANT_FIELD_NAMES)
	writer = csv.DictWriter(csvfile, fieldnames=RESTAURANT_FIELD_NAMES)

	writer.writeheader()
	for restaurant in restaurants:
		writer.writerow(vars(restaurant))