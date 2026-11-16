# Cross-Language Specification — Web Server Log Analyzer

## Algorithm
Parse standard Combined Log Format (CLF) web server access logs and compute operational metrics in a single O(n) pass:
- Total valid requests (`total_requests`)
- Malformed lines skipped (`malformed_lines`)
- Unique client IP addresses (`unique_visitors`)
- HTTP error count (`status >= 400`) and percentage (`error_rate`, rounded to 2 decimal places)
- Total response bytes (`total_bytes_transferred`, treating `-` as `0`)
- Top 3 most requested endpoints (`top_endpoints`, sorted by count descending, ties broken alphabetically)

## Inputs
- UTF-8 plain text log file or newline-delimited string (`\n` or `\r\n`)
- Line pattern: `<ip> - - [<timestamp>] "<method> <path> <protocol>" <status_code> <bytes>`
- Example line: `192.168.1.10 - - [16/Nov/2026:14:22:01 +0000] "GET /api/v1/users HTTP/1.1" 200 1024`

## Outputs
A deterministic JSON object containing:
- `total_requests` (integer, default `0`)
- `malformed_lines` (integer, default `0`)
- `unique_visitors` (integer, default `0`)
- `error_count` (integer, default `0`)
- `error_rate` (float, default `0.0`)
- `total_bytes_transferred` (integer, default `0`)
- `top_endpoints` (array of `{"path": string, "count": integer}`, default `[]`)

Example JSON output:
`{"total_requests": 4, "malformed_lines": 0, "unique_visitors": 3, "error_count": 1, "error_rate": 25.0, "total_bytes_transferred": 3584, "top_endpoints": [{"path": "/api/v1/users", "count": 2}, {"path": "/index.html", "count": 1}, {"path": "/login", "count": 1}]}`

## Edge Cases
1. **Empty File / Empty Input:** Returns all counters as `0`, `error_rate: 0.0`, and `top_endpoints: []` without division-by-zero errors.
2. **Malformed Log Entries:** Lines missing quotes, truncated fields, or non-numeric HTTP status codes are skipped and increment `malformed_lines`.
3. **Missing Byte Size (`-`):** Responses with `-` instead of a byte count (e.g., HTTP 204 or 304) are valid requests and add `0` to `total_bytes_transferred`.
4. **Tie-Breaking in Top Endpoints:** Endpoints with identical counts are sorted lexicographically (alphabetically) by `path` ascending for identical output across all languages.
5. **Blank / Whitespace Lines:** Empty lines are safely ignored without crashing the parser.

## Test Cases
1. **log_empty.txt** (Empty input `""`) -> `total_requests: 0`, `malformed_lines: 0`, `unique_visitors: 0`, `error_count: 0`, `error_rate: 0.0`, `total_bytes_transferred: 0`, `top_endpoints: []`
2. **log_standard.txt** (4 valid requests from 3 IPs, one 401 error, total 4120 bytes) -> `total_requests: 4`, `malformed_lines: 0`, `unique_visitors: 3`, `error_count: 1`, `error_rate: 25.0`, `total_bytes_transferred: 4120`, `top_endpoints: [{"path": "/home", "count": 2}, {"path": "/about", "count": 1}, {"path": "/login", "count": 1}]`
3. **log_malformed.txt** (1 valid `200` line + 2 corrupted lines with invalid status `NaN` and missing fields) -> `total_requests: 1`, `malformed_lines: 2`, `unique_visitors: 1`, `error_count: 0`, `error_rate: 0.0`, `total_bytes_transferred: 64`, `top_endpoints: [{"path": "/health", "count": 1}]`
4. **log_dash_bytes.txt** (1 request with `204 -` and 1 request with `500 512` on `/api/item/9`) -> `total_requests: 2`, `malformed_lines: 0`, `unique_visitors: 2`, `error_count: 1`, `error_rate: 50.0`, `total_bytes_transferred: 512`, `top_endpoints: [{"path": "/api/item/9", "count": 2}]`
5. **log_all_errors.txt** (4 error requests `404, 403, 502, 503` on `/a`, `/b`, `/c`, `/d`, 100 bytes each) -> `total_requests: 4`, `malformed_lines: 0`, `unique_visitors: 1`, `error_count: 4`, `error_rate: 100.0`, `total_bytes_transferred: 400`, `top_endpoints: [{"path": "/a", "count": 1}, {"path": "/b", "count": 1}, {"path": "/c", "count": 1}]`
