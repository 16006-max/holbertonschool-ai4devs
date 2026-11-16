# Fix Validation Report

## bug1.py
- **Original Issue**: Off-by-one slicing error (`transactions[start_index:-1]`) dropped the last element and shifted the start index, while a mutable default argument (`history=[]`) leaked state across calls.
- **Fix Applied**: Replaced `history=[]` with `history=None` (initializing a new list per call) and simplified slicing to `transactions[-count:]` with a guard for `count <= 0` or empty input.
- **Test Results**: All 5 test cases passed (`count=2`, `count=1`, `count > len(list)`, `count=0`, and isolated `history` state verification).

## bug2.js
- **Original Issue**: Missing `await` on `fetchTaxRate()` caused `NaN` tax calculations, and `i <= cartItems.length` caused a `TypeError` out-of-bounds array access.
- **Fix Applied**: Added `await` before `fetchTaxRate()` and changed the loop bound to `i < cartItems.length`.
- **Test Results**: All 2 async test cases passed (standard multi-item discounted cart returning `1115.1` and empty cart returning `0`).

## bug3.java
- **Original Issue**: Calling `role.toLowerCase()` prior to a null check threw a `NullPointerException`, and using `==` compared string references rather than values.
- **Fix Applied**: Added upfront null/empty checks for `username` and `role`, and replaced `==` with `"admin".equalsIgnoreCase(role.trim())`.
- **Test Results**: All 4 test cases passed (heap-allocated `"ADMIN"` string, `null` role, `null` username, and non-admin `"user"` role).

## bug4.sql
- **Original Issue**: Unparenthesized `OR is_active = 1` broke operator precedence (returning all active users), and `deleted_at != '2026-01-01'` excluded rows where `deleted_at` was `NULL`.
- **Fix Applied**: Replaced `OR` with `AND is_active = 1` and changed the soft-delete check to `AND deleted_at IS NULL`.
- **Test Results**: All 3 SQL test scenarios passed (matching active non-deleted user returned, active user with different email excluded, and soft-deleted user with `deleted_at` timestamp excluded).

## bug5.py
- **Original Issue**: Strict `>` comparison excluded boundary scores equal to `60`, and empty `scores` input raised a `ZeroDivisionError`.
- **Fix Applied**: Added an empty-list guard (`if not scores: return 0.0`) and changed the threshold comparison from `>` to `>=`.
- **Test Results**: All 4 test cases passed (boundary score `60`, mixed pass/fail scores, empty list `[]`, and 0% pass rate).
