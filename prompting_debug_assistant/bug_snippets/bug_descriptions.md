# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The start index is calculated with an extra +1, so the function always returns n-1 items instead of n.

## Bug 2 – bug2.js
**Intended Behavior**: Return the average of an array of numbers (0 for an empty array).  
**Issue Type**: Misuse of data types.  
**Notes**: With string values, `+=` concatenates instead of adding, giving a wrong result. An empty array returns NaN because of 0/0.

## Bug 3 – bug3.py
**Intended Behavior**: Count how many times each word appears in a text.  
**Issue Type**: Runtime exception.  
**Notes**: A KeyError is raised because the key is not initialized before incrementing.

## Bug 4 – bug4.c
**Intended Behavior**: Calculate the sum of the 5 elements of an array.  
**Issue Type**: Off-by-one / loop logic issue.  
**Notes**: The loop condition `i <= 5` reads one element past the end of the array (undefined behavior).

## Bug 5 – bug5.js
**Intended Behavior**: Return "even" or "odd" depending on the number.  
**Issue Type**: Syntax error.  
**Notes**: The closing brace of the `if` block is missing before `else`, so the code does not run.

## Bug 6 – bug6.py
**Intended Behavior**: Convert a numeric score into a letter grade (A, B, C or F).  
**Issue Type**: Logical error.  
**Notes**: The conditions are in the wrong order, so any score of 50 or above returns "C".
