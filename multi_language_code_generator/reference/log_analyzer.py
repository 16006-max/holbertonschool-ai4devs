import re
from collections import Counter
from typing import Any

LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+\S+\s+\[(?P<timestamp>[^\]]+)\]\s+'
    r'"(?P<method>[A-Z]+)\s+(?P<path>\S+)\s+(?P<protocol>[^"]+)"\s+'
    r'(?P<status>\d{3})\s+(?P<bytes>\d+|-)$'
)


class LogAnalyzer:
    """Reference implementation for parsing Combined Log Format (CLF) web logs."""

    def parse_line(self, line: str) -> dict[str, Any] | None:
        """Parse a single log line. Returns None if the line is malformed."""
        stripped = line.strip()
        if not stripped:
            return None

        match = LOG_PATTERN.match(stripped)
        if not match:
            return None

        raw_bytes = match.group("bytes")
        byte_count = 0 if raw_bytes == "-" else int(raw_bytes)

        return {
            "ip": match.group("ip"),
            "timestamp": match.group("timestamp"),
            "method": match.group("method"),
            "path": match.group("path"),
            "protocol": match.group("protocol"),
            "status": int(match.group("status")),
            "bytes": byte_count,
        }

    def analyze(self, lines: list[str]) -> dict[str, Any]:
        """Analyze a list of raw log lines and return aggregated metrics."""
        total_requests = 0
        malformed_lines = 0
        unique_visitors: set[str] = set()
        error_count = 0
        total_bytes = 0
        endpoint_counts: Counter[str] = Counter()

        for line in lines:
            if not line or not line.strip():
                continue

            parsed = self.parse_line(line)
            if parsed is None:
                malformed_lines += 1
                continue

            total_requests += 1
            unique_visitors.add(parsed["ip"])
            total_bytes += parsed["bytes"]
            endpoint_counts[parsed["path"]] += 1

            if parsed["status"] >= 400:
                error_count += 1

        error_rate = (
            round((error_count / total_requests) * 100, 2)
            if total_requests > 0
            else 0.0
        )

        sorted_endpoints = sorted(
            endpoint_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )[:3]

        top_endpoints = [
            {"path": path, "count": count} for path, count in sorted_endpoints
        ]

        return {
            "total_requests": total_requests,
            "malformed_lines": malformed_lines,
            "unique_visitors": len(unique_visitors),
            "error_count": error_count,
            "error_rate": error_rate,
            "total_bytes_transferred": total_bytes,
            "top_endpoints": top_endpoints,
        }

    def analyze_text(self, text: str) -> dict[str, Any]:
        """Convenience helper to analyze a multiline string."""
        if not text:
            return self.analyze([])
        return self.analyze(text.splitlines())
