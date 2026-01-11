import unittest

from cows import generate_num


class TestGenerateNum(unittest.TestCase):
    
    def test_length_is_4(self):
        result = generate_num()
        self.assertEqual(len(result), 4)
    
    def test_only_digits(self):
        result = generate_num()
        self.assertTrue(result.isdigit())
    
    def test_no_duplicate_digits(self):
        result = generate_num()
        self.assertEqual(len(result), len(set(result)))
    
    def test_returns_string(self):
        result = generate_num()
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()
