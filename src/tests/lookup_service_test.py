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

    def test_own_public_ip_is_valid(self):
        self.assertTrue([validators.ipv6(self.lookup.find_own_public_ip()[11:-8]) or \
            validators.ipv4(self.lookup.find_own_public_ip()[11:-8])].count(True) == 1)

    def test_local_ip_is_valid(self):
        self.assertTrue([validators.ipv6(self.lookup.find_local_ip()[11:-8]) or \
            validators.ipv4(self.lookup.find_local_ip()[11:-8])].count(True) == 1)

    def test_mac_is_valid(self):
        self.assertTrue(validators.mac_address(self.lookup.find_mac()[5:-6]))

    def test_domain_ping(self):
        self.assertEqual(self.lookup.domain_ping("melkki.cs.helsinki.fi")[:7], 
        "Latency")

    def test_ip_ping(self):
        self.assertEqual(self.lookup.domain_ping("128.214.9.98")[:7], 
        "Latency")

    def test_available_domain_ping(self):
        self.assertEqual(self.lookup.domain_ping("available1w2domain3w4.org"), 
        "Domain is available or nameservers failed to answer query")

    def test_available_domain_ping_ip(self):
        self.assertEqual(self.lookup.domain_ping("96.118.139.252"), 
        "Domain is available or nameservers failed to answer query")

    def test_invalid_domain_ping(self):
        self.assertEqual(self.lookup.domain_ping("invalid#domain%,,com"), 
        "Invalid hostname or IP")

    def test_invalid_ip_ping(self):
        self.assertEqual(self.lookup.domain_ping("961.1181.139.252"), 
        "Invalid hostname or IP")

    def test_timeout_domain_ping(self):
        self.assertEqual(self.lookup.domain_ping("game8.jp"), 
        "Pinging process timed out (severe latency or packet loss)")

    def test_timeout_ip_ping(self):
        self.assertEqual(self.lookup.domain_ping("18.177.117.55"), 
        "Pinging process timed out (severe latency or packet loss)")
