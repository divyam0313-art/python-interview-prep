# Q24. Longest Common Subsequence

**Level:** Medium  |  **Topic:** Dynamic Programming (2-D)

## Problem

Given two strings `a` and `b`, return the length of their longest common subsequence (characters in the same order, not necessarily contiguous).

## Signature

```python
def lcs_length(a: str, b: str) -> int:
```

## Examples

```
lcs_length("abcde", "ace")  ->  3   # "ace"
lcs_length("abc", "def")    ->  0
```

## Expected efficiency

O(len(a) x len(b)).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
