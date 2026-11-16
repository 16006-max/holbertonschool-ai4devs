# Pull Request: Add Multi-Criteria Task Filtering & Search Feature

## Summary
Implements a structured task filtering and keyword search module (`filter_tasks`) that allows users to filter tasks by `status`, `priority`, `due_date` range (`due_before` / `due_after`), and case-insensitive `keyword` matching. Includes input validation and a comprehensive unit test suite.

## Changes
- Added `filter_tasks()` and `validate_date()` functions in `task_filter.py`
- Added custom `TaskFilterError` exception handling for invalid statuses, priorities, and malformed date strings
- Added 5 unit tests in `TestTaskFilter` covering status filtering, combined priority/date filtering, keyword search, and error edge cases
- Verified all unit tests pass via `python3 -m unittest task_filter.py`

## Context
- **Lines of Code:** ~145 LOC (including docstrings and unit tests)
- **Related Issue:** #42
- **Motivation:** As task lists grow, users need a reliable and validated way to narrow down deliverables by deadline and urgency without manually scanning the full backlog.
