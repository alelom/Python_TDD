import unittest

class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket(self):
        basket = Basket([]) # passing an empty list "of items" as argument.
        self.assertEqual(basket.total(), 0)