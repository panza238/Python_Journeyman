"""Unit tests corresponding to the resolver package"""
import unittest
from resolver import DNSResolver
# This import will NOT fail if PYTHONPATH is correctly set!


class ResolverTests(unittest.TestCase):
    """All Resolver Tests"""

    def setUp(self) -> None:
        self._domain = 'google.com'

    def tearDown(self) -> None:
        pass

    def test_class_exists(self):
        test_instance = DNSResolver()

    def ip_validation(self, ip):
        """helper function to validate the IP"""
        # Check that it returns a string
        self.assertIsInstance(ip, str)
        # Check that it returns 4 octets
        ip_octets = ip.split('.')
        self.assertEqual(len(ip_octets), 4)

    def test_returns_valid_ip(self):
        """test whether the returned IP is valid"""
        test_instance = DNSResolver()
        ip = test_instance.resolve(self._domain)
        self.ip_validation(ip)

    def test_callable_instance(self):
        """test wether the instance is callable"""
        test_instance = DNSResolver()
        # Here I am implementing a callable instance. It is invoking the __call__ method defined in the class
        ip = test_instance(self._domain)
        self.ip_validation(ip)


if __name__ == '__main__':
    unittest.main()
