import unittest
from src.food import Food

class TestFood(unittest.TestCase):
	
	def setUp(self):
		self.food = Food("Pie", 5.0, 2.0)
	
	def test_food_has_name(self):
		self.assertEqual("Pie", self.food.name)
	
	def test_food_has_price(self):
		self.assertEqual(5.0, self.food.price)
	
	def test_food_has_rejuvenation_level(self):
		self.assertEqual(2.0, self.food.rejuvenation_level)
	
