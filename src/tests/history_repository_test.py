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
        self.history.insert("melkki.cs.helsinki.fi", "128.214.9.98", "Latency: 0.432 ms")
        self.assertEqual(self.history.fetch_all(),\
            [["melkki.cs.helsinki.fi", "128.214.9.98", "0.432 ms", self.current_date]])

    def test_inserts_and_fetches_multiple_rows_correctly(self):
        self.history.insert("melkki.cs.helsinki.fi", "128.214.9.98", "Latency: 0.432 ms")
        self.history.insert("australia.gov.au", "18.67.105.98", "Latency: 275.004 ms")
        self.assertEqual(self.history.fetch_all(),\
            [["australia.gov.au", "18.67.105.98", "275 ms", self.current_date],\
              ["melkki.cs.helsinki.fi", "128.214.9.98", "0.432 ms", self.current_date]])

    def test_clears_table(self):
        self.history.insert("melkki.cs.helsinki.fi", "128.214.9.98", "Latency: 0.432 ms")
        self.history.insert("australia.gov.au", "18.67.105.98", "Latency: 275.004 ms")
        self.history.clear_all()
        self.assertEqual(self.history.fetch_all(), [])
