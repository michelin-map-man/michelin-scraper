
class CardProcessor:
	"""The card object should be a Beautiful Soup object."""
	def __init__(self, card):
		self.card = card

	def get_title_element(self):
		if not hasattr(self, "title_element"):
			self.title_element = self.card.find("h3", class_="card__menu-content--title").find("a")
		return self.title_element

	def get_name(self):
		return self.get_title_element().string.strip()

	def get_restaurant_uri(self):
		return self.get_title_element()["href"]

	def get_lat(self):
		return self.card["data-lat"]

	def get_lng(self):
		return self.card["data-lng"]

	def get_location(self):
		return self.card.find("div", class_="card__menu-footer--location").string.strip()

	def get_price_element(self):
		if not hasattr(self, "price_element"):
			self.price_element = self.card.find("div", class_="card__menu-footer--price")
		return self.price_element

	def get_price(self):
		return self.get_price_element().string.split()[0].strip()

	def get_type(self):
		return self.get_price_element().string.split()[-1].strip()

	def get_rating(self):
		rating_images = self.card.find_all("img", class_="michelin-award", src=self.is_bib_or_star)
		count = len(rating_images)
		if count == 0:
			return "Unrated"
		elif count == 1 and "bib-gourmand" in rating_images[0]["src"]:
			return "Bib Gourmand"
		else:
			return f"{count} star"

	def is_bib_or_star(self, src):
		value = "bib-gourmand" in src or "1star" in src
		return value

	def get_google_link(self):
		query = f"{self.get_name()}+{self.get_location()}".replace(" ", "+")
		return f"https://www.google.com/search?q={query}"