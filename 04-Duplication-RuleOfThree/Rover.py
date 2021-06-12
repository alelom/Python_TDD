from dataclasses import *

# frozen=True makes the class immutable. 
# The class can be modified internally with a copy of itself using dataclasses.replace().
@dataclass(frozen=True)
class Rover:
    facing : str
    
    def go(self, instruction):
        if (self.facing == "N"):
            return replace(self, facing = "E")
        
        if (self.facing == "E"):
            return replace(self, facing = "S")