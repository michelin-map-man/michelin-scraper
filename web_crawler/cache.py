from pathlib import Path
from datetime import datetime
import dateutil.relativedelta

from countries.country_provider import Country



class Cache:
	
	def __init__(self, country: Country):
		self.country = country
		self.cache_path_string = f"./cached_countries/{self.country.shortcode}"
		self.cache_hits = 0
		self.cache_misses = 0
		Path(f"{self.cache_path_string}/restaurants").mkdir(parents=True, exist_ok=True)


	def get_or_load(self, file_name, loading_function):
		path = self.get_path(file_name)
		if self.isCacheValid(path):
			self.cache_hits = self.cache_hits + 1
			return path.read_bytes()
		
		self.cache_misses = self.cache_misses + 1
		path.unlink(missing_ok=True)
		data = loading_function()
		path.touch()
		path.write_bytes(data)
		return data

	def isCacheValid(self, path):
		if not path.is_file():
			return False

		create_date = datetime.fromtimestamp(path.stat().st_ctime)
		months_ago = dateutil.relativedelta.relativedelta(datetime.now(), create_date).months
		if months_ago < 6:
			return True
		return False

	def get_path(self, file_name):
		return Path(f"{self.cache_path_string}/{file_name}")

	def print_metrics(self):
		print(f"Hits: {self.cache_hits}. Misses: {self.cache_misses}")

