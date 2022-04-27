import unittest
from currency_converter import CurrencyConverter

url = "https://api.exchangerate-api.com/v4/latest/USD"
curr = CurrencyConverter(url)


class TestCurrencyConverter(unittest.TestCase):
    def test_calc_rates(self):
        self.assertEqual(round(curr.calc_rates('KES','USD', 100),4), 0.8623)

   
if __name__ == "__main__":
    unittest.main()
        