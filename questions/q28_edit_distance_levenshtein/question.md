# Q28. Edit Distance (Levenshtein)

**Level:** Hard  |  **Topic:** Dynamic Programming (2-D)

## Problem

Given two words, return the minimum number of single-character operations (insert, delete, replace) needed to convert `a` into `b`.

## Signature

```python
def edit_distance(a: str, b: str) -> int:
```

## Examples

```
edit_distance("horse", "ros")  ->  3
edit_distance("intention", "execution")  ->  5
```

## Expected efficiency

O(len(a) x len(b)).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
