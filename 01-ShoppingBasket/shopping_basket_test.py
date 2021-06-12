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
        
    def test_single_item_quantity_one(self):
        basket = Basket([Item(100.0, 1)])
        self.assertEqual(basket.total(), 100.0)
        
    def test_two_items_quantity_one(self):
        basket = Basket([Item(100.0, 1), Item(100.0, 1)])
        self.assertEqual(basket.total(), 200.0)
        
    def test_two_items_quantity_two(self):
        basket = Basket([Item(100.0, 2), Item(100.0, 2)])
        self.assertEqual(basket.total(), 400.0)

# Needed if the IDE does not capture tests.
if __name__ == '__main__':
    unittest.main()