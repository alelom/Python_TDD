import unittest

class ShoppingBasketTest(unittest):
    def test_empty_basket(self):
        basket = Basket([]) # passing an empty list "of items" as argument.