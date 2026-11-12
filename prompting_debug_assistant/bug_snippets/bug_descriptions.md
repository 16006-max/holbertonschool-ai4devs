# Bug Descriptions

## Bug 1 – bug1.py
- Intended behavior: Return the last n items of a list.
- Issue type: Off-by-one error.
- Notes: The start index is calculated with an extra +1, so the function always returns n-1 items instead of n. For example, last_n_items([1, 2, 3, 4, 5], 3) returns [4, 5] instead of [3, 4, 5].

## Bug 2 – bug2.js
- Intended behavior: Return the average of an array of numbers (0 for an empty array).
- Issue type: Misuse of data types.
- Notes: With string values, += concatenates instead of adding, so the result is wrong. An empty array returns NaN because of 0/0.

## Bug 3 – bug3.py
- Intended behavior: Count how many times each word appears in a text.
- Issue type: Runtime exception.
- Notes: A KeyError is raised because the key is not initialized before it is incremented.

## Bug 4 – bug4.c
- Intended behavior: Calculate the sum of the 5 elements of an array.
- Issue type: Off-by-one / loop logic issue.
- Notes: The loop condition i <= 5 reads one element past the end of the array, which is undefined behavior.

## Bug 5 – bug5.js
- Intended behavior: Return "even" or "odd" depending on the number.
- Issue type: Syntax error.
- Notes: The closing brace of the if block is missing before else, so the code does not run.

## Bug 6 – bug6.py
- Intended behavior: Convert a numeric score into a letter grade (A, B, C or F).
- Issue type: Logical error.
- Notes: The conditions are in the wrong order, so any score of 50 or above returns "C" and the B and A branches are never reached.
