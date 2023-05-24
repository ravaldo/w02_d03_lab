import unittest
from src.pub import Pub
from src.drink import Drink
from src.food import Food
from src.customer import Customer

class TestPub(unittest.TestCase):
	
	def setUp(self):
		self.beer = Drink("beer", 5.0, 2.8)
		self.wine = Drink("wine", 4.0, 1.4)
		self.vodka = Drink("vodka", 3.5, 1)
		
		self.pie = Food("Pie", 5.0, 2.0)
		self.burger = Food("burger", 10.0, 4.0)
		self.crisps = Food("crisps", 1.0, 0.5)
		
		stock = { 
			self.beer : 10, 
			self.wine : 20, 
			self.vodka : 30,
			self.pie : 10,
			self.burger : 0,
			self.crisps : 2
			}
		
		self.pub = Pub("The Prancing Pony", 100.5, stock)
		
		self.fred = Customer("Fred", 5.0, 17)
		self.harry = Customer("Harry", 1.0, 50)
		self.james = Customer("James", 100.0, 30)
	
	def test_pub_has_name(self):
		self.assertEqual("The Prancing Pony", self.pub.name)
	
	def test_till_value(self):
		self.assertEqual(100.5, self.pub.till)
	
	def test_increase_till(self):
		self.pub.increase_till(2.5)
		self.assertEqual(103.0, self.pub.till)
	
	def test_in_stock(self):
		self.assertEqual(True, self.pub.in_stock(self.beer))
		
	def test_not_in_stock(self):
		self.assertEqual(False, self.pub.in_stock(self.burger))
		
	def test_customer_too_drunk(self):
		self.james.drunkenness = 7
		self.assertEqual(True, self.pub.is_too_drunk(self.james))
		
	def test_customer_of_age(self):
		self.assertEqual(False, self.pub.is_of_age(self.fred))
	
	def test_sell_drink(self):
		self.pub.sell_drink(self.james, self.beer)
		self.assertEqual(105.5, self.pub.till)
		self.assertEqual(95, self.james.wallet)
		self.assertEqual(2.8, self.james.drunkenness)
		self.assertEqual(9, self.pub.stock[self.beer])
	
	def test_sell_food_customer_short_cash(self):
		self.pub.sell_food(self.harry, self.pie)
		self.assertEqual(self.pub.till, 100.5)
		self.assertEqual(self.pub.stock[self.pie], 10)
		self.assertEqual(self.harry.wallet, 1)
	
	def test_sell_food_customer_has_cash(self):
		self.james.drunkenness = 5
		self.pub.sell_food(self.james, self.pie)
		self.assertEqual(self.pub.till, 105.5)
		self.assertEqual(self.pub.stock[self.pie], 9)
		self.assertEqual(self.james.wallet, 95)
		self.assertEqual(self.james.drunkenness, 3)
	
	def test_stock_value(self):
		self.assertEqual(self.pub.stock_value(), 287)
	
	
		
	