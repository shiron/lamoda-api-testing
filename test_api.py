import unittest
from client_api import ClientAPI

URL = 'http://apigw.lamoda.ru/json/get_product_product_recommendations'

class TestGetReccomend(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = ClientAPI(URL)

    def test_correct_sku_without_limit(self):
        """

        """
        status_code, response = TestGetReccomend.api.get_recommendations(sku='lo019emjgz27')

        self.assertEqual(200, status_code,
                         'Wrong response code, expected 200, but actual is {}'.format(status_code))
        self.assertTrue(len(response) > 0,
                        'The method return zero goods')

    def test_correct_sku_correct_limit(self):
        """

        """
        status_code, response = TestGetReccomend.api.get_recommendations(sku='lo019emjgz27', limit=2)
        self.assertEqual(200, status_code,
                         'Wrong response code, expected 200, but actual is {}'.format(status_code))
        self.assertEqual(2, len(response),
                         'The method return wrong count of goods {}'.format(len(response)))

    def test_wrong_sku(self):
        """

        """
        status_code, response = TestGetReccomend.api.get_recommendations(sku='0_0')
        self.assertEqual(400, status_code,
                         'Wrong response code, expected 400, but actual is {}'.format(status_code))
        self.assertEqual('Client.RECOMMENDATIONS_NOT_AVAILABLE', response['faultcode'],
                         'Wrong message in faultcode')
        self.assertEqual('Recommendation service is not available', response['faultstring'],
                         'Wrong message in faultstring')

    def test_wrong_limit(self):
        """

        """
        status_code, response = TestGetReccomend.api.get_recommendations(sku='lo019emjgz27', limit=-1)
        self.assertEqual(400, status_code,
                         'Wrong response code, expected 400, but actual is {}'.format(status_code))
        self.assertEqual('Client.ValidationError', response['faultcode'],
                         'Wrong message in faultcode')
        self.assertEqual('The value \'-1\' could not be validated.', response['faultstring'],
                         'Wrong message in faultstring')


if __name__ == 'main':
    unittest.main()