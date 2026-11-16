# Cross-Language Specification — Web Server Log Analyzer

## 1. Algorithm Description
The **Log Analyzer** parses standard Combined Log Format (CLF) web server access logs and aggregates key operational metrics in a single $O(n)$ pass over the input lines.

For each valid log line:
1. Extract the client IP address, HTTP method, requested path, HTTP status code, and response size in bytes.
2. Increment `total_requests`.
3. Add the client IP to a set of `unique_visitors`.
4. Count status codes `>= 400` as errors and calculate `error_rate` as `(error_count / total_requests) * 100`, rounded to 2 decimal places.
5. Track request frequency per endpoint (`path`) and determine `top_endpoints` sorted by count descending (ties broken lexicographically by path ascending), limited to the top 3.
6. Sum response bytes into `total_bytes_transferred` (treating `-` size as `0`).

---

## 2. Input Format
- **Source:** UTF-8 encoded plain text file or newline-delimited string (`\n` or `\r\n`).
- **Line Pattern:**
  `<ip> - - [<timestamp>] "<method> <path> <protocol>" <status_code> <bytes>`
- **Example Line:**
  `192.168.1.10 - - [16/Nov/2026:14:22:01 +0000] "GET /api/v1/users HTTP/1.1" 200 1024`

---

## 3. Output Format
A deterministic JSON object with the following schema:

```json
{
  "total_requests": 4,
  "malformed_lines": 0,
  "unique_visitors": 3,
  "error_count": 1,
  "error_rate": 25.0,
  "total_bytes_transferred": 3584,
  "top_endpoints": [
    { "path": "/api/v1/users", "count": 2 },
    { "path": "/index.html", "count": 1 },
    { "path": "/login", "count": 1 }
  ]
}
