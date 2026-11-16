## AI Review Log

### Inline Comments

- **(line 18) [Security / Input Validation]:** `validate_date()` accepts dates without checking reasonable year bounds (e.g., year `0001` or `9999`). Consider enforcing realistic calendar range validation to prevent malformed or nonsensical dates from entering downstream logic.
- **(line 27) [Maintainability]:** The `filter_tasks()` function takes 6 positional/keyword parameters. Consider grouping filter criteria into a `TaskFilterCriteria` dataclass or `TypedDict` to improve readability and simplify future extensions.
- **(line 47) [Security / Type Safety]:** Checking `if status is not None` allows empty strings (`""`) to trigger a `TaskFilterError`, whereas passing `keyword=""` silently bypasses filtering. Normalize empty strings consistently across all optional string parameters.
- **(line 53) [Performance]:** `validate_date(due_before)` and `validate_date(due_after)` are parsed correctly outside the loop, which is good, but `task.get("due_date")` inside the loop is re-parsed on every `filter_tasks()` call. Pre-parsing or caching `datetime` objects on task ingestion would avoid repeated `strptime` overhead.
- **(line 62) [Maintainability]:** The loop in `filter_tasks()` uses multiple sequential `if ... continue` blocks. Extracting helper predicates (e.g., `_matches_date_range()`, `_matches_keyword()`) will reduce cyclomatic complexity and make each filter rule independently testable.
- **(line 69) [Security / Error Handling]:** If a task dictionary in `tasks` contains a corrupted or non-ISO `due_date` string, `validate_date(task_due_str)` raises an unhandled `TaskFilterError` mid-iteration, aborting the entire query instead of safely skipping or logging the malformed record.
- **(line 76) [Performance]:** Calling `str(task.get("title", "")).lower()` and `str(task.get("description", "")).lower()` allocates new strings for every task on each search. For larger datasets, pre-normalizing searchable text or short-circuiting earlier can reduce memory allocations.
- **(line 85) [Maintainability]:** Separating unit tests (`TestTaskFilter`) into a dedicated `tests/test_task_filter.py` file rather than bundling them inside the production `task_filter.py` module follows standard Python project structure.

### Global Feedback

- **[Security Persona]:** Add defensive type checks to ensure `tasks` is an iterable of dictionaries (e.g., guarding against `None` or non-dict elements causing `AttributeError` on `.get()`), and sanitize `keyword` length (e.g., max 200 characters) to mitigate ReDoS/CPU abuse in public API endpoints.
- **[Performance Persona]:** For large task backlogs (10,000+ items), consider converting `filter_tasks()` into a generator (`yield task`) or supporting indexed lookups by `status` and `priority` instead of performing a full linear scan ($O(n)$) on every filter invocation.
- **[Maintainability Persona]:** Recommend splitting `filter_tasks()` into smaller, single-responsibility helper functions and adding explicit `Logging` hooks when tasks are skipped due to missing or invalid fields.
- **[Testing Coverage]:** Expand `TestTaskFilter` to cover edge cases such as an empty `tasks=[]` input list, whitespace-only `keyword="   "`, `None` values inside task fields (`title=None`), and combined multi-filter queries using all 5 filter parameters simultaneously.
