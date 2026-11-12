# Reflection on AI-Assisted Debugging

## Introduction
In this project I collected six buggy snippets in Python, JavaScript and C, asked an AI assistant to diagnose each one, applied the fixes, tested them and documented the results in structured reports. The goal was to measure how useful AI is as a debugging partner and where it still needs a human.

## AI Strengths
The AI was fastest on bugs with a clear signal. The syntax error in bug5.js and the KeyError in bug3.py were diagnosed immediately, because the error message points almost directly at the cause. The off-by-one in bug1.py and the wrong condition order in bug6.py were also solved on the first attempt, and the explanations used concrete values, for example that `last_n_items([1, 2, 3, 4, 5], 3)` returned `[4, 5]` instead of `[3, 4, 5]`. The AI also offered useful alternatives, such as `collections.Counter` for bug 3 and `sizeof` instead of a hardcoded array size in bug 4. Compared with searching forums, this was clearly faster.

## AI Weaknesses
The hardest cases had more than one problem or no visible symptom. Bug 2 had two issues, string concatenation and a division by zero on an empty array, so a quick answer could easily fix only one of them. Bug 4 is silent: reading past the end of the array is undefined behavior, so the program may still print a plausible sum and the code alone cannot prove the failure. Some alternatives also had hidden pitfalls. The shortcut `items[-n:]` looks correct for bug 1, but it returns the whole list when `n = 0`, so it needs a guard. The main fix was simple:

```diff
- start = len(items) - n + 1
+ start = len(items) - n
```

## Human Role
I did not trust any suggestion until I ran it. I executed every fixed file and checked boundary values such as n = 0 and the scores 90, 70, 50 and 49, which were not part of the original examples. Humans also choose the best fix: I kept the one-line `counts.get` change for bug 3 instead of rewriting with `Counter`, because it leaves the original code intact. Documentation needed attention too: a duplicated paste in my debug log made an automated review fail, and no AI prevented that. Finally, only the developer knows the intended behavior, for example what a function should return when `n = 0`.

## Conclusion
AI made the process faster overall, especially for diagnosis and explanation, but it did not remove the need for testing. My trust was high for syntax and logic errors with clear symptoms, and lower for memory and edge-case problems. In real-world debugging I would use AI as a fast first reviewer, then confirm every fix with tests and my own understanding of the requirements.
