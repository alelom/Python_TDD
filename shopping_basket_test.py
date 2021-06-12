import unittest
import dataclasses

@dataclasses.dataclass 
class Basket(object): #dataclass is used for classes used mostly for holding data.
    items: list # This syntax uses dataclass to add an `items` property w/ getters and constructor injection. `item` is of the generic python `list` type. 
    
    def total(self):
        return 0

class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket(self):
        basket = Basket([]) # passing an empty list "of items" as argument.
        self.assertEqual(basket.total(), 0)