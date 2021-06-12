from logging import StringTemplateStyle
import unittest
import dataclasses
from unittest.main import main

@dataclasses.dataclass
class CD:
    artist : str = "artist"
    title : str = "title"
    quantity : int = 0
    
    def get_stock_count(self):
        return self.quantity
    
    def buy(self, q):
        self.quantity -= q

class Test_BuyCD(unittest.TestCase):
    def test_buy_cd_inStock(self):
        cd = CD("John", "title", 10)
        cd.buy(5)
        self.assertEqual(5, cd.get_stock_count())
        

if __name__ == "__main__":
    unittest.main()