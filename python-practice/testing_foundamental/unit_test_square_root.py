import unittest

# Buggy function
def square(x):
    return x * 3

class TestSquareFunction(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(square(2), 4)  # Expected 4, but will get 6

    def test_square_zero(self):
        self.assertEqual(square(0), 0)  # This one will pass

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)  # Expected 9, but will get -9

    def test_square_invalid_input(self):
        with self.assertRaises(TypeError):
            square("a")  # Should raise an error if input isn't a number

if __name__ == "__main__":
    unittest.main()
