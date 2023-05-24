import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestCustomer(unittest.TestCase):
	
	def setUp(self):
		self.customer = Customer("Jimbo", 5.0, 50)
		self.beer = Drink("beer", 4.0, 2.8)
		self.pie = Food("Pie", 6.0, 2.0)
	
	def test_cust_has_name(self):
		self.assertEqual("Jimbo", self.customer.name)
	
	def test_cust_has_wallet(self):
		self.assertEqual(5.0, self.customer.wallet)
		
	def test_cust_has_age(self):
		self.assertEqual(50, self.customer.age)
	
	def test_can_afford_postive(self):
		self.assertEqual(True, self.customer.can_afford_item(self.beer))
		
	def test_can_afford_negative(self):
		self.assertEqual(False, self.customer.can_afford_item(self.pie))
	
	def test_buy_drink(self):
		self.customer.buy_drink(self.beer)
		self.assertEqual(1, self.customer.wallet)
		self.assertEqual(2.8, self.customer.drunkenness)
	
	def test_buy_food(self):
		fred = Customer("Fred", 6.0, 20)
		fred.drunkenness = 3		
		fred.buy_food(self.pie)
		self.assertEqual(0, fred.wallet)
		self.assertEqual(1, fred.drunkenness)
		
	
		
		
	