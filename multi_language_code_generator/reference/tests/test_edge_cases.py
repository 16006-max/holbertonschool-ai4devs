import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from log_analyzer import LogAnalyzer


class TestLogAnalyzerEdgeCases(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    def test_large_byte_values(self):
        lines = [
            '10.0.0.1 - - [16/Nov/2026:10:00:01 +0000] "GET /video.mp4 HTTP/1.1" 200 104857600',
            '10.0.0.2 - - [16/Nov/2026:10:00:02 +0000] "GET /archive.zip HTTP/1.1" 200 52428800',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_bytes_transferred"], 157286400)
        self.assertEqual(result["total_requests"], 2)

    def test_mixed_valid_and_corrupted_stream(self):
        lines = [
            "",
            "INVALID_LINE_1",
            '192.168.0.1 - - [16/Nov/2026:10:00:01 +0000] "GET /ok HTTP/1.1" 200 128',
            "INVALID_LINE_2",
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["malformed_lines"], 2)

    def test_all_5xx_server_errors(self):
        lines = [
            '10.1.1.1 - - [16/Nov/2026:10:00:01 +0000] "POST /pay HTTP/1.1" 500 256',
            '10.1.1.2 - - [16/Nov/2026:10:00:02 +0000] "POST /pay HTTP/1.1" 502 256',
            '10.1.1.3 - - [16/Nov/2026:10:00:03 +0000] "POST /pay HTTP/1.1" 504 256',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_count"], 3)
        self.assertEqual(result["error_rate"], 100.0)


if __name__ == "__main__":
    unittest.main()
