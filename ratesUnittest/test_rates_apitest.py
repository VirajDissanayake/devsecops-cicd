import unittest
import requests
from rates.rates import create_app

class TestRatesAPI(unittest.TestCase):
    def test_1_get_average_rates(self):
        url = "http://127.0.0.1:3000/rates"
        payload = {'orig_code': 'CNGGZ', 'dest_code': 'EETLL', 'date_from': '2021-01-01', 'date_to': '2021-01-31'}
        req = requests.get(url, params=payload)
        self.assertEqual(req.status_code, 200)

