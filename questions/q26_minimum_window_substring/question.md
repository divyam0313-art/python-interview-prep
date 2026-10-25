# Q26. Minimum Window Substring

**Level:** Hard  |  **Topic:** Sliding Window (variable)

## Problem

Given strings `s` and `t`, return the smallest substring of `s` that contains every character of `t` (including duplicates). Return an empty string if no such window exists.

## Signature

```python
def min_window(s: str, t: str) -> str:
```

## Examples

```
min_window("ADOBECODEBANC", "ABC")  ->  "BANC"
min_window("a", "aa")  ->  ""
```

## Expected efficiency

O(len(s) + len(t)).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
