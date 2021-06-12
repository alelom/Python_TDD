from typing import List
import unittest
import dataclasses

@dataclasses.dataclass
class Movie:
    pass

class Library:
    def __init__(self, catalogue = []):
        self._catalogue = catalogue
    
    def donate(self, movie):
        self._catalogue.append(movie)

    def contains(self, movie):
        return movie in self._catalogue
        

class DonateMovieTest(unittest.TestCase):
    def test_donate_movie(self):
        movie = Movie()
        library = Library([])
        library.donate(movie)
        
        # Start backwards from the assertion.
        self.assertTrue(library.contains(movie))


# Needed if the IDE does not capture tests.
if __name__ == '__main__':
    unittest.main()