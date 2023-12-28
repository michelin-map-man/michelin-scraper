
RESTAURANT_FIELD_NAMES = [
	"rating",
	"name",
	"price",
	"type",
	"lat",
	"lng",
	"google",
	"website",
	"review"
]

class Restaurant:
	def __init__(self, card_processor, restauarant_processor):
		self.rating = card_processor.get_rating()
		self.name = card_processor.get_name()
		self.price = card_processor.get_price()
		self.type = card_processor.get_type()
		self.lat = card_processor.get_lat()
		self.lng = card_processor.get_lng()
		self.google = card_processor.get_google_link()
		self.website = restauarant_processor.get_restaurant_website()
		self.review = restauarant_processor.get_restaurant_review()