import unittest
from dataclasses import *
from Rover import *

    
class MarsRoverTest(unittest.TestCase):
    def test_turn_right_NtoE(self):
        rover = Rover("N")
        rover = rover.go("R") #go to the right.
        self.assertEqual("E", rover.facing)
        
    def test_turn_right_EtoS(self):
        rover = Rover("E")
        rover = rover.go("R") #go to the right.
        self.assertEqual("S", rover.facing)
        
    # we've here introduced duplication.
    # Before introducing a refactoring to abstract away and reduce duplication,
    # it's a good idea to keep adding duplication for a while.
    # This is because if we refactor duplication too early
    # we might be introducing the wrong abstraction.
    # On the other hand, adding too much duplication takes too long to refactor.
    # Rule of three: introduce 3 duplicated cases before refactor and abstract.

# Needed if the IDE does not capture tests.
if __name__ == '__main__':
    unittest.main()