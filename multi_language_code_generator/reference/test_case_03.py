import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from log_analyzer import LogAnalyzer


class TestCase03(unittest.TestCase):
    def test_valid_request(self):
        analyzer = LogAnalyzer()
        res = analyzer.analyze(['127.0.0.1 - - [16/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" 200 100'])
        self.assertEqual(res["total_requests"], 1)


if __name__ == "__main__":
    unittest.main()
