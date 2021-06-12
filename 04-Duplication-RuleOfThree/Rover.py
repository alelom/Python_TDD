from dataclasses import *

# frozen=True makes the class immutable. 
# The class can be modified internally with a copy of itself using dataclasses.replace().
@dataclass(frozen=True)
class Rover:
    facing : str
    
    def turn_right(self):
        directions = ["N", "E", "S", "W"] #sorted clockwise
        
        return replace(self, facing = directions[directions.index(self.facing) + 1])