from src.drink import *


class Pub:
	def __init__(self, name, amount, stock):
		self.name = name
		self.till = amount
		self.min_age = 18
		self.max_drunkenness = 6
		self.stock = stock
	
	def increase_till(self, amount):
		self.till += amount
	
	def is_of_age(self, customer):
		return True if customer.age >= self.min_age else False
	
	def is_too_drunk(self, customer):
		return True if customer.drunkenness >= self.max_drunkenness else False
	
	def in_stock(self, drink):
		for d in self.stock.keys():
			if d.name == drink.name:
				if self.stock[d] >= 1:
					return True
		return False
	
	def sell_drink(self, customer, drink):
		if self.in_stock(drink):
			if self.is_of_age(customer):
				if customer.can_afford_item(drink):
					if not self.is_too_drunk(customer):
						self.increase_till(drink.price)
						self.stock[drink] -= 1
						customer.buy_drink(drink)
		
	def sell_food(self, customer, food):
		if self.in_stock(food):
			if customer.can_afford_item(food):
					self.increase_till(food.price)
					self.stock[food] -= 1
					customer.buy_food(food)		
		
	