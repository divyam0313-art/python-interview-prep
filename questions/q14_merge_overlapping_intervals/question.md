# Q14. Merge Overlapping Intervals

**Level:** Medium  |  **Topic:** Sorting / Intervals

## Problem

Given a list of intervals `[start, end]`, merge all overlapping intervals and return the non-overlapping result.

## Signature

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
```

## Examples

```
merge_intervals([[1,3],[2,6],[8,10],[15,18]])  ->  [[1,6],[8,10],[15,18]]
merge_intervals([[1,4],[4,5]])  ->  [[1,5]]   # touching counts as overlap
```

## Expected efficiency

O(n log n).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
