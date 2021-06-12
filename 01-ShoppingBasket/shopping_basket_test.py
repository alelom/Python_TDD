import unittest
import dataclasses
from shopping_basket import Basket

@dataclasses.dataclass
class Item:
    unit_price : float
    quantity: 1

class Test_ShoppingBasket(unittest.TestCase):
    def test_empty_basket(self):
        basket = Basket([]) # passing an empty list "of items" as argument.
        self.assertEqual(basket.total(), 0)
        
    def test_single_item_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)

if __name__ == '__main__':
    unittest.main()