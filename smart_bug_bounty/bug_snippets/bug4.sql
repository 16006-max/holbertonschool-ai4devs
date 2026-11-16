-- Vulnerable stored procedure / query template for searching active user accounts
-- Intended Behavior: Return non-deleted users matching a specific email and role

SELECT id, username, email, role
FROM users
WHERE email = 'user@example.com'
  AND role = 'member'
  -- Bug 1: Operator precedence bug (`OR` without parentheses bypasses email/role filters)
  OR is_active = 1
  -- Bug 2: Comparing NULL with `!=` fails to include rows where deleted_at IS NULL
  AND deleted_at != '2026-01-01';
