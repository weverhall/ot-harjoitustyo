import unittest
import validators
from services.lookup_service import NetworkLookup

# Domain names and IPs tested on April 24, 2022
class TestLookupService(unittest.TestCase):
    def setUp(self):
        self.lookup = NetworkLookup()

    def test_finds_available_domain(self):
        self.assertEqual(self.lookup.domain_lookup("available1w2domain3w4.org"), 
        "Domain is available!")

    def test_finds_available_ip(self):
        self.assertEqual(self.lookup.domain_lookup("96.118.139.252"), 
        "Domain is available!")

    def test_finds_invalid_domain(self):
        self.assertEqual(self.lookup.domain_lookup("invalid#domain%,,com"), 
        "Invalid domain name or IP")

    def test_finds_invalid_ip(self):
        self.assertEqual(self.lookup.domain_lookup("961.1181.139.252"), 
        "Invalid domain name or IP")

    def test_finds_taken_domain(self):
        self.assertEqual(self.lookup.domain_lookup("amazon.com")[:23], 
        "Domain is already taken")

    def test_finds_taken_ip(self):
        self.assertEqual(self.lookup.domain_lookup("128.214.222.24")[:23], 
        "Domain is already taken")

    def test_finds_taken_domain_correct_ip(self):
        self.assertEqual(self.lookup.domain_lookup("melkki.cs.helsinki.fi")[:42], 
        "Domain is already taken (IP: 128.214.9.98)")

    def test_finds_taken_domain_correct_fqdn(self):
        self.assertEqual(self.lookup.domain_lookup("128.214.9.98")[:53], 
        "Domain is already taken (FQDN: melkki.cs.helsinki.fi)")

    def test_own_public_ip_is_valid(self):
        self.assertTrue([validators.ipv6(self.lookup.find_own_public_ip()[11:-8]) or \
            validators.ipv4(self.lookup.find_own_public_ip()[11:-8])].count(True) == 1)

    def test_local_ip_is_valid(self):
        self.assertTrue([validators.ipv6(self.lookup.find_local_ip()[11:-8]) or \
            validators.ipv4(self.lookup.find_local_ip()[11:-8])].count(True) == 1)

    def test_mac_is_valid(self):
        self.assertTrue(validators.mac_address(self.lookup.find_mac()[5:-6]))

