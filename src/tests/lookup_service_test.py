import unittest
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
        "Invalid IP or domain name")

    def test_finds_invalid_ip(self):
        self.assertEqual(self.lookup.domain_lookup("961.1181.139.252"), 
        "Invalid IP or domain name")

    def test_finds_taken_domain(self):
        self.assertEqual(self.lookup.domain_lookup("amazon.com")[:23], 
        "Domain is already taken")

    def test_finds_taken_ip(self):
        self.assertEqual(self.lookup.domain_lookup("128.214.222.24")[:23], 
        "Domain is already taken")

    def test_finds_taken_domain_correct_ip(self):
        self.assertEqual(self.lookup.domain_lookup("melkki.cs.helsinki.fi"), 
        "Domain is already taken (host/proxy IP: 128.214.9.98)")

    def test_finds_taken_domain_correct_hostname(self):
        self.assertEqual(self.lookup.domain_lookup("128.214.9.98"), 
        "Domain is already taken (host/proxy name: melkki.cs.helsinki.fi)")