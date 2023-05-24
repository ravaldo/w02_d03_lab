import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
	
	def setUp(self):
		self.drink = Drink("Beer", 5.5, 2.8)
	
	def test_drink_has_name(self):
		self.assertEqual("Beer", self.drink.name)
	
	def test_drink_has_price(self):
		self.assertEqual(5.5, self.drink.price)
	
	def test_drink_has_alcohol_level(self):
		self.assertEqual(2.8, self.drink.alcohol_level)
	
