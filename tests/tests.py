import unittest

from cows import generate_num, counting_cows_and_bulls


class TestCounting(unittest.TestCase):

    def test_four_cows(self):
        result = counting_cows_and_bulls("2314", "1432")
        assert "4 cow(s)" in result
        assert "0 buuul(s)" in result

    def test_four_bulls(self):
        result = counting_cows_and_bulls("2345", "2345")
        assert "0 cow(s)" in result
        assert "4 buuul(s)" in result

    def test_no_matches(self):
        result = counting_cows_and_bulls("1234", "5678")
        assert "0 cow(s)" in result
        assert "0 buuul(s)" in result

    def test_two_cows_bulls(self):
        # comp: 1234
        # play: 1243
        # bulls: 1,2
        # cows: 3,4
        result = counting_cows_and_bulls("1234", "1243")
        assert "2 cow(s)" in result
        assert "2 buuul(s)" in result


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
