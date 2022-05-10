import unittest
import datetime
import validators
from services.lookup_service import NetworkLookup
from repositories.history_repository import(
    history_repository as default_history_repository)


class TestLookupService(unittest.TestCase):
    """Domain names and IPs tested on May 7, 2022"""

    def setUp(self, history=default_history_repository):
        self.history = history
        self.lookup = NetworkLookup()
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        history.clear_all()

    def test_finds_available_domain(self):
        self.assertEqual(self.lookup.domain_lookup("available1w2domain3w4.org"),
                         "Domain is available!")

    def test_finds_available_ip(self):
        self.assertEqual(self.lookup.domain_lookup("96.118.139.252"),
                         "Domain is available (or PTR record is invalid)")

    def test_finds_invalid_domain(self):
        self.assertEqual(self.lookup.domain_lookup("invalid#domain%,,com"),
                         "Invalid domain name or IP")

    def test_finds_invalid_ip(self):
        self.assertEqual(self.lookup.domain_lookup("961.1181.139.252"),
                         "Invalid domain name or IP")

    def test_finds_taken_domain(self):
        self.assertEqual(self.lookup.domain_lookup("amazon.com")[:15],
                         "Domain is taken")

    def test_finds_taken_ip(self):
        self.assertEqual(self.lookup.domain_lookup("128.214.222.24")[:15],
                         "Domain is taken")

    def test_finds_taken_domain_correct_ip(self):
        self.assertEqual(self.lookup.domain_lookup("melkki.cs.helsinki.fi")[:36],
                         "Domain is taken (IPv4: 128.214.9.98)")

    def test_finds_taken_domain_correct_fqdn(self):
        self.assertEqual(self.lookup.domain_lookup("128.214.9.98")[:45],
                         "Domain is taken (FQDN: melkki.cs.helsinki.fi)")

    def test_times_out_domain_ping(self):
        self.assertEqual(self.lookup.domain_lookup("game8.jp")[-57:],
                         "Pinging process timed out (severe latency or packet loss)")

    def test_handles_unreachable_domain(self):
        self.assertEqual(self.lookup.domain_lookup("124.240.242.119")[-53:],
                         "Pinging process failed (destination port unreachable)")

    def test_own_public_ip_is_valid(self):
        self.assertTrue([validators.ipv6(self.lookup.find_own_public_ip()[11:-8]) or
                         validators.ipv4(self.lookup.find_own_public_ip()[11:-8])].count(True) == 1)

    def test_local_ip_is_valid(self):
        self.assertTrue([validators.ipv6(self.lookup.find_local_ip()[11:-8]) or
                         validators.ipv4(self.lookup.find_local_ip()[11:-8])].count(True) == 1)

    def test_mac_is_valid(self):
        self.assertTrue(validators.mac_address(self.lookup.find_mac()[5:-6]))

    def test_lookup_fetches_row_correctly(self):
        self.history.insert("melkki.cs.helsinki.fi",
                            "128.214.9.98", "Latency: 0.432 ms")
        self.assertEqual(self.lookup.fetch_history(),
                         [["melkki.cs.helsinki.fi", "128.214.9.98", "0.432 ms", self.current_date]])

    def test_lookup_clears_table(self):
        self.history.insert("melkki.cs.helsinki.fi",
                            "128.214.9.98", "Latency: 0.432 ms")
        self.lookup.clear_history()
        self.assertEqual(self.lookup.fetch_history(), [])
