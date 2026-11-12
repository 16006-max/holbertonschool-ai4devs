# Bug Reports

## Bug Report – bug1.py
- File name: bug1.py (fixed version: bug1_fixed.py)
- Summary: The function last_n_items returns one item too few. With n = 3 it returns [4, 5] instead of [3, 4, 5].
- Root cause: Off-by-one error. The start index was calculated as `len(items) - n + 1`, so the loop skipped the first element of the last n items.
- Resolution: The AI suggested changing the line to `start = len(items) - n`. No manual edits were needed.
  - Before: `start = len(items) - n + 1`
  - After: `start = len(items) - n`
- Lesson learned: Always test boundary values (n = 0, n = len(items)) when working with indexes and ranges.

## Bug Report – bug2.js
- File name: bug2.js (fixed version: bug2_fixed.js)
- Summary: calculateAverage returns a wrong number for an array of strings and NaN for an empty array.
- Root cause: Misuse of data types. With string values, `total += numbers[i]` concatenates instead of adding ("0" + "10" + "20" + "30" = "0102030"). For an empty array the result is 0 / 0 = NaN.
- Resolution: The AI suggested converting each value with `Number(numbers[i])` and returning 0 early for an empty array. No manual edits were needed.
  - Before: `total += numbers[i];`
  - After: `total += Number(numbers[i]);` plus `if (numbers.length === 0) { return 0; }`
- Lesson learned: JavaScript does not stop you from mixing types. Convert input explicitly and handle empty input before dividing.

## Bug Report – bug3.py
- File name: bug3.py (fixed version: bug3_fixed.py)
- Summary: word_frequency crashes with a KeyError on the first word.
- Root cause: Runtime exception. `counts[word] += 1` reads a key that does not exist in the dictionary yet.
- Resolution: The AI suggested `counts[word] = counts.get(word, 0) + 1`. It also listed collections.Counter as an alternative, which worked too. The get() version was chosen because it changes only one line. No manual edits were needed.
  - Before: `counts[word] += 1`
  - After: `counts[word] = counts.get(word, 0) + 1`
- Lesson learned: Initialize dictionary keys (or use get() and defaultdict/Counter) before updating them.

## Bug Report – bug4.c
- File name: bug4.c (fixed version: bug4_fixed.c)
- Summary: The program may print a wrong sum or behave unpredictably instead of printing 15.
- Root cause: Off-by-one loop error. The condition `i <= 5` runs six times, so `numbers[5]` reads one element past the end of the 5-element array, which is undefined behavior.
- Resolution: The AI suggested changing the condition to `i < 5`. It also mentioned using `sizeof(numbers) / sizeof(numbers[0])` instead of a hardcoded size. No manual edits were needed.
  - Before: `for (i = 0; i <= 5; i++)`
  - After: `for (i = 0; i < 5; i++)`
- Lesson learned: Array indexes go from 0 to size - 1. In C there is no bounds check, so out-of-range reads fail silently.

## Bug Report – bug5.js
- File name: bug5.js (fixed version: bug5_fixed.js)
- Summary: The script does not run at all and throws a SyntaxError.
- Root cause: Syntax error. The closing brace of the `if` block is missing before `else`, so the braces do not match.
- Resolution: The AI suggested writing `} else {` instead of `else {`. A ternary version (`n % 2 === 0 ? "even" : "odd"`) was mentioned as an alternative. No manual edits were needed.
  - Before: `return "even"; else {`
  - After: `return "even"; } else {`
- Lesson learned: Read the error message and line number first, and use an editor with bracket matching to catch missing braces.

## Bug Report – bug6.py
- File name: bug6.py (fixed version: bug6_fixed.py)
- Summary: get_grade returns "C" for every score of 50 or above, so get_grade(95) gives "C" instead of "A".
- Root cause: Logical error. The conditions are checked from the lowest threshold to the highest, so `score >= 50` is always true first and the "B" and "A" branches are never reached.
- Resolution: The AI suggested checking the highest threshold first (90, then 70, then 50). No manual edits were needed.
  - Before: `if score >= 50` checked first, then `>= 70`, then `>= 90`
  - After: `if score >= 90`, then `elif score >= 70`, then `elif score >= 50`, else "F"
- Lesson learned: In an if/elif chain, the order of conditions matters. Order them from most specific to most general and test boundary values (90, 70, 50, 49).

## AI-generated vs manual work
- AI-generated: all diagnoses and all suggested fixes listed above.
- Manual: running every fixed file, checking the outputs against the expected results, and recording them in fix_validation.md. No manual code edits were needed beyond the AI suggestions.
