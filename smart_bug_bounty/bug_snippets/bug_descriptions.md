# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return the last `count` items from a list of transactions and track query logs per call without sharing state across invocations.
- **Current Issue**: Off-by-one slicing error (`transactions[start_index:-1]`) drops the final element and shifts the start index, plus a mutable default argument (`history=[]`) leaks log entries across separate function calls.

## bug2.js
- **Intended Behavior**: Asynchronously fetch the current tax rate, apply a percentage discount to each item in the shopping cart, and return the final total including tax.
- **Current Issue**: Missing `await` keyword on `fetchTaxRate()` causes arithmetic operations on a `Promise` object (`NaN`), and an off-by-one loop condition (`i <= cartItems.length`) throws a `TypeError` when accessing `cartItems[cartItems.length]`.

## bug3.java
- **Intended Behavior**: Safely verify whether a given user has the `"admin"` role (case-insensitive) and return `false` if either `username` or `role` is `null`.
- **Current Issue**: Calling `role.toLowerCase()` prior to checking for `null` throws a `NullPointerException`, and comparing strings with `==` checks reference equality instead of value equality (`.equals()`).

## bug4.sql
- **Intended Behavior**: Retrieve active, non-deleted user accounts matching both a target email address and a specific role.
- **Current Issue**: Missing parentheses around the `OR` condition alters operator precedence so all active users are returned regardless of email/role, and `deleted_at != '2026-01-01'` excludes records where `deleted_at` is `NULL`.

## bug5.py
- **Intended Behavior**: Calculate the percentage of student scores greater than or equal to the passing threshold (`60`), returning `0.0` if the input list is empty.
- **Current Issue**: Using strict `>` instead of `>=` misclassifies boundary scores equal to `60` as failing, and dividing by `len(scores)` without an empty-list guard raises a `ZeroDivisionError`.
