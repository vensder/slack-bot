import unittest
import plugins.ssl_expiry as test_ssl

class SSLExpiry(unittest.TestCase):
    def test_get_ssl_expiry_datetime(self):
        self.assertTrue(test_ssl.get_ssl_expiry_datetime("google.com"))

class SSLExpiryV2(unittest.TestCase):
    def test_get_ssl_expiry_datetime_v2(self):
        self.assertTrue(test_ssl.get_ssl_expiry_datetime_v2("google.com"))
