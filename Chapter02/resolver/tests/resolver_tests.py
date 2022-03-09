"""Unit tests corresponding to the resolver package"""
import unittest
from resolver import DNSResolver
# This import will NOT fail if PYTHONPATH is correctly set!


class ResolverTests(unittest.TestCase):
    """All Resolver Tests"""

    def setUp(self) -> None:
        self._domain = 'google.com'
        self._domain_list = ('linkedin.com', 'yahoo.com', 'youtube.com')

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

    def test_resolve_args(self):
        """test added *args functionality"""
        test_instance = DNSResolver()
        test_instance.resolve_args(*self._domain_list)
        # * here would be the complementary operation to *args
        # * "unpacks" the values on the list and passes them one by one to the function (as *args!!)
        self.assertEqual(len(test_instance._cache), 3)

    def test_resolve_kwargs(self):
        """test **kwargs method"""
        test_instance = DNSResolver()
        test_instance.resolve_kwargs(host=self._domain)
        self.assertEqual(len(test_instance._cache), 1)
        test_instance.resolve_kwargs(host_list=self._domain_list)
        self.assertEqual(len(test_instance._cache), 4)
        # just like *iterable "unpacks" values into a function as args
        # **dict "unpacks" the dict values into a function as kwargs
        # my_function(**dict) <=> my_function(dict.key1=dict[key1], dict.key2=dict[key2], ...)


if __name__ == '__main__.py':
    unittest.main()
