# Benchmark Coding Tasks — Copilot Productivity Sprint

## Task 1 - User Registration CRUD Endpoint
**Requirements**: Implement a REST API endpoint `POST /users` that validates incoming user data, checks for duplicate emails in memory/database, hashes the password, and stores the new user.  
**Inputs**: JSON payload `{"name": "string", "email": "string", "password": "string"}`  
**Outputs**: JSON object containing the created user (`id`, `name`, `email`, `created_at`) without exposing the password.  
**Acceptance Criteria**:  
- Returns HTTP `201 Created` with the generated user ID on valid input.  
- Returns HTTP `400 Bad Request` if `name` is empty, `email` format is invalid, or `password` is shorter than 8 characters.  
- Returns HTTP `409 Conflict` if the email is already registered.  
- Unit tests achieve at least 90% code coverage.

---

## Task 2 - Log File Parser & Anomaly Aggregator
**Requirements**: Write a Python function `analyze_logs(log_lines: list[str]) -> dict` that parses structured server log entries (`[TIMESTAMP] [LEVEL] [SERVICE] Message`), counts occurrences per log level, identifies the top 3 most frequent error messages, and flags services with an error rate exceeding 20%.  
**Inputs**: A list of raw log strings, e.g., `["2026-11-16T10:00:00Z ERROR auth-service Invalid token", ...]`  
**Outputs**: A dictionary containing `level_counts`, `top_errors`, and `flagged_services`.  
**Acceptance Criteria**:  
- Accurately parses valid log lines and safely skips malformed lines without crashing.  
- Correctly calculates error percentages per service (`ERROR` count / total logs for that service).  
- Handles empty input lists gracefully by returning zeroed counts and empty lists.  
- Executes in $O(n)$ time complexity where $n$ is the number of log lines.

---

## Task 3 - Rate Limiter (Token Bucket Algorithm)
**Requirements**: Implement a thread-safe `RateLimiter` class using the Token Bucket algorithm to throttle API requests per client IP address.  
**Inputs**: Configuration parameters (`capacity: int`, `refill_rate_per_sec: float`) and method call `allow_request(client_id: str) -> bool`.  
**Outputs**: Boolean (`True` if request is permitted and a token is consumed; `False` if the bucket is empty).  
**Acceptance Criteria**:  
- Allows bursts up to `capacity` tokens immediately.  
- Refills tokens accurately over elapsed time without exceeding `capacity`.  
- Isolates token buckets independently per `client_id`.  
- Passes all unit tests simulating time progression and concurrent access.
