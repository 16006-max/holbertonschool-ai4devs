import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from log_analyzer import LogAnalyzer


class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()

    # Test Case 1: Empty input list
    def test_empty_input(self):
        result = self.analyzer.analyze([])
        self.assertEqual(
            result,
            {
                "total_requests": 0,
                "malformed_lines": 0,
                "unique_visitors": 0,
                "error_count": 0,
                "error_rate": 0.0,
                "total_bytes_transferred": 0,
                "top_endpoints": [],
            },
        )

    # Test Case 2: Blank and whitespace-only lines
    def test_whitespace_only_lines(self):
        result = self.analyzer.analyze(["", "   ", "\n", "\t"])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["malformed_lines"], 0)
        self.assertEqual(result["error_rate"], 0.0)

    # Test Case 3: Standard mixed traffic
    def test_standard_mixed_traffic(self):
        lines = [
            '10.0.0.1 - - [16/Nov/2026:10:00:01 +0000] "GET /home HTTP/1.1" 200 1500',
            '10.0.0.2 - - [16/Nov/2026:10:00:02 +0000] "POST /login HTTP/1.1" 401 320',
            '10.0.0.1 - - [16/Nov/2026:10:00:03 +0000] "GET /home HTTP/1.1" 200 1500',
            '10.0.0.3 - - [16/Nov/2026:10:00:04 +0000] "GET /about HTTP/1.1" 200 800',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 4)
        self.assertEqual(result["malformed_lines"], 0)
        self.assertEqual(result["unique_visitors"], 3)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["error_rate"], 25.0)
        self.assertEqual(result["total_bytes_transferred"], 4120)
        self.assertEqual(
            result["top_endpoints"],
            [
                {"path": "/home", "count": 2},
                {"path": "/about", "count": 1},
                {"path": "/login", "count": 1},
            ],
        )

    # Test Case 4: Malformed lines handling
    def test_malformed_lines(self):
        lines = [
            "CORRUPTED_ENTRY_NO_IP",
            '172.16.0.5 - - [16/Nov/2026:11:00:00 +0000] "GET /health HTTP/1.1" 200 64',
            '172.16.0.5 - - [16/Nov/2026:11:00:05 +0000] "BAD_REQUEST_FORMAT" NaN -',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)
        self.assertEqual(result["malformed_lines"], 2)
        self.assertEqual(result["unique_visitors"], 1)
        self.assertEqual(result["total_bytes_transferred"], 64)

    # Test Case 5: Dash ('-') byte sizes (e.g. HTTP 204/304)
    def test_dash_byte_sizes(self):
        lines = [
            '203.0.113.4 - - [16/Nov/2026:12:00:00 +0000] "DELETE /api/item/9 HTTP/1.1" 204 -',
            '203.0.113.8 - - [16/Nov/2026:12:00:01 +0000] "GET /api/item/9 HTTP/1.1" 500 512',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["error_count"], 1)
        self.assertEqual(result["error_rate"], 50.0)
        self.assertEqual(result["total_bytes_transferred"], 512)

    # Test Case 6: 100% error rate and top 3 truncation with alphabetical tie-breaking
    def test_all_errors_and_tie_breaking(self):
        lines = [
            '198.51.100.1 - - [16/Nov/2026:13:00:00 +0000] "GET /d HTTP/1.1" 503 100',
            '198.51.100.1 - - [16/Nov/2026:13:00:01 +0000] "GET /b HTTP/1.1" 403 100',
            '198.51.100.1 - - [16/Nov/2026:13:00:02 +0000] "GET /c HTTP/1.1" 502 100',
            '198.51.100.1 - - [16/Nov/2026:13:00:03 +0000] "GET /a HTTP/1.1" 404 100',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_rate"], 100.0)
        self.assertEqual(
            result["top_endpoints"],
            [
                {"path": "/a", "count": 1},
                {"path": "/b", "count": 1},
                {"path": "/c", "count": 1},
            ],
        )

    # Test Case 7: 0% error rate with 2xx and 3xx statuses
    def test_zero_errors_with_redirects(self):
        lines = [
            '10.0.0.1 - - [16/Nov/2026:14:00:00 +0000] "GET /old HTTP/1.1" 301 0',
            '10.0.0.1 - - [16/Nov/2026:14:00:01 +0000] "GET /new HTTP/1.1" 200 2048',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_count"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["total_bytes_transferred"], 2048)

    # Test Case 8: Rounding precision for error_rate
    def test_error_rate_rounding(self):
        lines = [
            '10.0.0.1 - - [16/Nov/2026:14:00:00 +0000] "GET /a HTTP/1.1" 200 100',
            '10.0.0.1 - - [16/Nov/2026:14:00:01 +0000] "GET /a HTTP/1.1" 200 100',
            '10.0.0.1 - - [16/Nov/2026:14:00:02 +0000] "GET /a HTTP/1.1" 404 100',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["error_rate"], 33.33)

    # Test Case 9: Single valid line parse_line unit test
    def test_parse_single_valid_line(self):
        line = '192.168.1.10 - - [16/Nov/2026:14:22:01 +0000] "POST /api/v1/users HTTP/1.1" 201 512'
        parsed = self.analyzer.parse_line(line)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["ip"], "192.168.1.10")
        self.assertEqual(parsed["method"], "POST")
        self.assertEqual(parsed["path"], "/api/v1/users")
        self.assertEqual(parsed["status"], 201)
        self.assertEqual(parsed["bytes"], 512)

    # Test Case 10: Single invalid line parse_line returns None
    def test_parse_single_invalid_line(self):
        self.assertIsNone(self.analyzer.parse_line("not a valid log"))

    # Test Case 11: Query strings in endpoint paths
    def test_paths_with_query_parameters(self):
        lines = [
            '10.0.0.5 - - [16/Nov/2026:15:00:00 +0000] "GET /search?q=ai&page=1 HTTP/1.1" 200 1200',
            '10.0.0.6 - - [16/Nov/2026:15:00:01 +0000] "GET /search?q=ai&page=1 HTTP/1.1" 200 1200',
        ]
        result = self.analyzer.analyze(lines)
        self.assertEqual(
            result["top_endpoints"],
            [{"path": "/search?q=ai&page=1", "count": 2}],
        )

    # Test Case 12: analyze_text multiline string helper with CRLF endings
    def test_analyze_text_crlf(self):
        raw_text = (
            '10.0.0.1 - - [16/Nov/2026:16:00:00 +0000] "GET /ping HTTP/1.1" 200 10\r\n'
            '10.0.0.2 - - [16/Nov/2026:16:00:01 +0000] "GET /ping HTTP/1.1" 500 20\r\n'
        )
        result = self.analyzer.analyze_text(raw_text)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["unique_visitors"], 2)
        self.assertEqual(result["error_rate"], 50.0)
        self.assertEqual(result["total_bytes_transferred"], 30)


if __name__ == "__main__":
    unittest.main()
