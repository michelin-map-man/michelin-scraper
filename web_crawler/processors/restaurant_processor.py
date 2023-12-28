from bs4 import BeautifulSoup

class RestaurantProcessor:
	def __init__(self, html_content):
		self.soup = BeautifulSoup(html_content, "html.parser")

	def get_restaurant_website(self):
		element = self.soup.find("a", attrs={"data-event": "CTA_website"})
		if element is not None:
			return element["href"]
		return None

	def get_restaurant_review(self):
		return self.soup.find("div", class_="restaurant-details__description--text").find("p").string