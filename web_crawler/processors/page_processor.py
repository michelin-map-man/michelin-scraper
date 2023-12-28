from bs4 import BeautifulSoup
from web_crawler.processors import CardProcessor

class MichelinPageProcessor:

	def __init__(self, html_content):
		self.soup = BeautifulSoup(html_content, "html.parser")

	def are_more_pages(self):
		pagination = self.soup.find("ul", class_="pagination")
		next_page_icon = pagination.find("i", class_="fa-angle-right")
		if next_page_icon is None:
			return False
		# These will always be relative links...so in this case it will just look like
		# /us/en/selection/united-states/restaurants/page/2
		self.next_page_uri = next_page_icon.find_parent("a")["href"]
		return True

	def get_next_page_uri(self):
		if self.are_more_pages():
			return self.next_page_uri
		return None

	def get_card_processors(self):
		cards = self.soup.find_all("div", class_="card__menu")
		card_processors = []
		for card in cards:
			processor = CardProcessor(card)
			card_processors.append(processor)
		return card_processors