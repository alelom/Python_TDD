import unittest
from dataclasses import *
from Rover import *
from parameterized import parameterized, parameterized_class
    
class MarsRoverTest(unittest.TestCase):
    @parameterized.expand(
        [
            ("N", "E")
        ]
    )
    def test_turn_right_NtoE(self, start_dir, end_dir):
        rover = Rover(start_dir)
        rover = rover.turn_right() #go to the right.
        self.assertEqual(end_dir, rover.facing)
        
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