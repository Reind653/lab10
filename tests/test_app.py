import unittest
from app import greet
class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World from Reind Ballout"), "Hello, World from Reind Ballout!")
if __name__ == "__main__":
    unittest.main()
