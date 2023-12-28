import json

class Country:
	def __init__(self, country_dict):
		self.cname = country_dict["cname"]
		self.shortcode = country_dict["shortcode"]

	def __iter__(self):
		yield from {
			"cname": self.cname,
			"shortcode": self.shortcode
		}.items()

	def __str__(self):
		return json.dumps(dict(self), indent=2)

	def __repr__(self):
		return self.__str__()



class CountryProvider:
	"""docstring for CountryProvider"""
	def __init__(self):
		with open("countries/Countries.json", "r") as country_file:
			self.country_map = json.load(country_file)

	def get_country(self, country_name) -> Country:
		if country_name in self.country_map:
			return Country(self.country_map[country_name])
		raise Exception(f"No country named {country_name} found")

	
	def print(self):
		country_map = self.country_map
		new_country_map = {}
		for country_code in country_map:
			country = country_map[country_code]
			new_country_map[country["label"]] = {
				"cname": country["cname"],
				"shortcode": country_code
			}
		print(json.dumps(new_country_map, sort_keys=True, indent=2))
