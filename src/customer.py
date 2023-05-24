
class Customer:
	def __init__(self, name, wallet, age):
		self.name = name
		self.wallet = wallet
		self.age = age
		self.drunkenness = 0
		
	def reduce_wallet(self, amount):
		self.wallet -= amount
	
	def can_afford_item(self, item):
		return True if self.wallet >= item.price else False
	
	def buy_drink(self, drink):
		self.reduce_wallet(drink.price)
		self.drunkenness += drink.alcohol_level
		
	def buy_food(self, food):
		self.reduce_wallet(food.price)
		self.drunkenness -= food.rejuvenation_level
		if self.drunkenness < 0:	
			self.drunkenness = 0
		
