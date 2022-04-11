import unittest
from services.lookup_service import NetworkLookup

class TestLookupService(unittest.TestCase):
    def setUp(self):
        self.lookup = NetworkLookup()

    def test_finds_available_domain(self):
        self.assertEqual(self.lookup.domain_lookup("available1w2domain3w4.org"), 
        "Domain is available!")

    def test_finds_invalid_domain(self):
        self.assertEqual(self.lookup.domain_lookup("invalid#domain%,,com"), 
        "Invalid domain name, try again")

    def test_finds_taken_domain(self):
        self.assertEqual(self.lookup.domain_lookup("amazon.com")[0:23], 
        "Domain is already taken")

    def test_finds_taken_domain_correct_ip(self):
        self.assertEqual(self.lookup.domain_lookup("melkki.cs.helsinki.fi"), 
        "Domain is already taken (host/proxy IP: 128.214.9.98)")
        #aforementioned IP found and tested on April 11, 2022
