# test_app.py

import unittest
from app import square

class TestApp(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(5), 25)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-3), 9)

if __name__ == "__main__":
    unittest.main()
