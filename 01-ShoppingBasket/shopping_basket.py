import dataclasses
from typing import List
from item import Item
from functools import reduce

@dataclasses.dataclass 
class Basket: #dataclass is used for classes used mostly for holding data.
    items: List[Item] # This syntax uses dataclass to add an `items` property w/ getters and constructor injection. `item` is of the generic python `list` type. 
    
    def total(self):
        return reduce(lambda subTotal, item: subTotal + item.unit_price * item.quantity, self.items, 0)