import unittest
import datetime
from repositories.history_repository import(
    history_repository as default_history_repository)


class TestHistoryRepository(unittest.TestCase):
    def setUp(self, history=default_history_repository):
        self.history = history
        self.current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        history.clear_all()

    def test_fetches_nothing_when_table_empty(self):
        self.assertEqual(self.history.fetch_all(), [])

    def test_inserts_and_fetches_row_correctly(self):
        self.history.insert("melkki.cs.helsinki.fi",
                            "128.214.9.98", "Latency: 0.430 ms")
        self.assertEqual(self.history.fetch_all(),
                         [["melkki.cs.helsinki.fi", "128.214.9.98", "0.43 ms", self.current_date]])

    def test_inserts_and_fetches_multiple_rows_correctly(self):
        self.history.insert("melkki.cs.helsinki.fi",
                            "128.214.9.98", "Latency: 0.432 ms")
        self.history.insert("australia.gov.au",
                            "18.67.105.98", "Latency: 275.152 ms")
        self.history.insert(
            "discord.com", "162.159.136.232", "Latency: 5.001 ms")
        self.assertEqual(self.history.fetch_all(),
                         [["australia.gov.au", "18.67.105.98", "275.2 ms", self.current_date],
                          ["discord.com", "162.159.136.232",
                              "5 ms", self.current_date],
                          ["melkki.cs.helsinki.fi", "128.214.9.98", "0.432 ms", self.current_date]])

    def test_clears_table(self):
        self.history.insert("melkki.cs.helsinki.fi",
                            "128.214.9.98", "Latency: 0.432 ms")
        self.history.insert("australia.gov.au",
                            "18.67.105.98", "Latency: 275.004 ms")
        self.history.clear_all()
        self.assertEqual(self.history.fetch_all(), [])

    def test_ping_error_correct_output(self):
        self.history.insert("game8.jp", "13.230.198.34",
                            "Pinging process timed out (severe latency or packet loss)")
        self.assertEqual(self.history.fetch_all(),
                         [["game8.jp", "13.230.198.34", "?", self.current_date]])
