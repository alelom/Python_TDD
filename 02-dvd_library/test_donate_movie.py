from typing import List
import unittest
import dataclasses
from movie import Movie

class Library:
    def __init__(self, catalogue = []):
        self._catalogue = catalogue # encapsulated field. No way of doing encapsulation by using @dataclasses.dataclass
    
    def donate(self, movie):
        self._catalogue.append(movie)
        movie.copies +=1

    def contains(self, movie):
        return movie in self._catalogue
        

class DonateMovieTest(unittest.TestCase):
    
    def setUp(self):
        self.movie = Movie()
        self.library = Library([])
        self.library.donate(self.movie)
    
    def test_library_contains_movie(self):
        # Start backwards from the assertion.
        self.assertTrue(self.library.contains(self.movie))
        
    def test_library_contains_one_copy(self):
        self.assertEqual(1, self.movie.copies)


# Needed if the IDE does not capture tests.
if __name__ == '__main__':
    unittest.main()