-- Fixed SQL query for searching active, non-deleted user accounts
-- Intended Behavior:
-- Return active, non-deleted users matching both email and role.

SELECT
    id,
    username,
    email,
    role
FROM users
WHERE email = 'user@example.com'
  AND role = 'member'
  AND is_active = 1
  AND deleted_at IS NULL;
