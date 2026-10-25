# Q29. Longest Increasing Subsequence in O(n log n)

**Level:** Hard  |  **Topic:** DP + Binary Search

## Problem

Return the length of the longest strictly increasing subsequence of `nums`. Give the O(n^2) DP idea first, then the O(n log n) solution.

## Signature

```python
def length_of_lis(nums: list[int]) -> int:
```

## Examples

```
length_of_lis([10,9,2,5,3,7,101,18])  ->  4   # e.g. 2,3,7,18
length_of_lis([7,7,7])  ->  1
```

## Expected efficiency

O(n log n).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
