import unittest
import plugins.ssl_expiry as test_ssl


class SSLExpiry(unittest.TestCase):
    def test_get_ssl_expiry_datetime(self):
        self.assertTrue(test_ssl.get_ssl_expiry_datetime("google.com"))


class SSLExpiryV2(unittest.TestCase):
    def test_get_ssl_expiry_datetime_v2(self):
        self.assertTrue(test_ssl.get_ssl_expiry_datetime_v2("google.com"))


class SSLCompareYandex(unittest.TestCase):
    def test_both_yandex(self):
        self.assertEqual(test_ssl.get_ssl_expiry_datetime("yandex.ru"),
                         test_ssl.get_ssl_expiry_datetime_v2("yandex.ru"))


class SSLCompareGoogle(unittest.TestCase):
    def test_both_google(self):
        self.assertEqual(type(test_ssl.get_ssl_expiry_datetime("google.ru")),
                         type(test_ssl.get_ssl_expiry_datetime_v2("google.ru")))
