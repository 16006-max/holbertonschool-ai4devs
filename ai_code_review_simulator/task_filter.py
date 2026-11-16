"""
Task Filtering & Search Module
Provides filtering by status, priority, due date range, and keyword search.
"""

from datetime import datetime
from typing import List, Dict, Optional, Any
import unittest


VALID_STATUSES = {"todo", "in_progress", "done"}
VALID_PRIORITIES = {"low", "medium", "high"}


class TaskFilterError(ValueError):
    """Custom exception raised for invalid filter parameters."""


def validate_date(date_str: str) -> datetime:
    """Parse and validate an ISO format date string (YYYY-MM-DD)."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError as exc:
        raise TaskFilterError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD.") from exc


def filter_tasks(
    tasks: List[Dict[str, Any]],
    status: Optional[str] = None,
    priority: Optional[str] = None,
    due_before: Optional[str] = None,
    due_after: Optional[str] = None,
    keyword: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Filter a list of task dictionaries based on optional criteria.

    Args:
        tasks: List of task objects represented as dictionaries.
        status: Optional status filter ('todo', 'in_progress', 'done').
        priority: Optional priority filter ('low', 'medium', 'high').
        due_before: Optional inclusive upper bound date (YYYY-MM-DD).
        due_after: Optional inclusive lower bound date (YYYY-MM-DD).
        keyword: Optional case-insensitive substring search in title/description.

    Returns:
        A filtered list of matching task dictionaries.
    """
    if status is not None and status not in VALID_STATUSES:
        raise TaskFilterError(f"Invalid status '{status}'. Must be one of {VALID_STATUSES}.")

    if priority is not None and priority not in VALID_PRIORITIES:
        raise TaskFilterError(f"Invalid priority '{priority}'. Must be one of {VALID_PRIORITIES}.")

    before_dt = validate_date(due_before) if due_before else None
    after_dt = validate_date(due_after) if due_after else None

    if before_dt and after_dt and after_dt > before_dt:
        raise TaskFilterError("'due_after' cannot be later than 'due_before'.")

    normalized_kw = keyword.strip().lower() if keyword else None
    results = []

    for task in tasks:
        if status and task.get("status") != status:
            continue

        if priority and task.get("priority") != priority:
            continue

        task_due_str = task.get("due_date")
        if (before_dt or after_dt) and not task_due_str:
            continue

        if task_due_str and (before_dt or after_dt):
            task_due_dt = validate_date(task_due_str)
            if before_dt and task_due_dt > before_dt:
                continue
            if after_dt and task_due_dt < after_dt:
                continue

        if normalized_kw:
            title = str(task.get("title", "")).lower()
            desc = str(task.get("description", "")).lower()
            if normalized_kw not in title and normalized_kw not in desc:
                continue

        results.append(task)

    return results


class TestTaskFilter(unittest.TestCase):
    """Unit tests for the task filtering feature."""

    def setUp(self):
        self.sample_tasks = [
            {
                "id": 1,
                "title": "Design database schema",
                "description": "Create ERD for users and tasks",
                "status": "done",
                "priority": "high",
                "due_date": "2026-11-10",
            },
            {
                "id": 2,
                "title": "Implement API endpoints",
                "description": "Build REST routes for task CRUD",
                "status": "in_progress",
                "priority": "high",
                "due_date": "2026-11-18",
            },
            {
                "id": 3,
                "title": "Write unit tests",
                "description": "Ensure 90% coverage on filter module",
                "status": "todo",
                "priority": "medium",
                "due_date": "2026-11-22",
            },
            {
                "id": 4,
                "title": "Update README docs",
                "description": "Document setup steps",
                "status": "todo",
                "priority": "low",
                "due_date": None,
            },
        ]

    def test_filter_by_status(self):
        res = filter_tasks(self.sample_tasks, status="todo")
        self.assertEqual(len(res), 2)
        self.assertEqual([t["id"] for t in res], [3, 4])

    def test_filter_by_priority_and_due_date(self):
        res = filter_tasks(self.sample_tasks, priority="high", due_before="2026-11-15")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["id"], 1)

    def test_filter_by_keyword(self):
        res = filter_tasks(self.sample_tasks, keyword="api")
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["title"], "Implement API endpoints")

    def test_invalid_status_raises_error(self):
        with self.assertRaises(TaskFilterError):
            filter_tasks(self.sample_tasks, status="archived")

    def test_invalid_date_range_raises_error(self):
        with self.assertRaises(TaskFilterError):
            filter_tasks(self.sample_tasks, due_after="2026-11-25", due_before="2026-11-10")


if __name__ == "__main__":
    unittest.main()
