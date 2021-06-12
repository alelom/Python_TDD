import dataclasses

@dataclasses.dataclass 
class Basket(object): #dataclass is used for classes used mostly for holding data.
    items: list # This syntax uses dataclass to add an `items` property w/ getters and constructor injection. `item` is of the generic python `list` type. 
    
    def total(self):
        return 0