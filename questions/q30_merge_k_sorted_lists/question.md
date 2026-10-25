# Q30. Merge K Sorted Lists

**Level:** Hard  |  **Topic:** Heap / K-way Merge

## Problem

Given k sorted lists, merge them into one sorted list efficiently. Discuss what changes if the lists are huge or streamed from disk.

## Signature

```python
def merge_k_sorted(lists: list[list[int]]) -> list[int]:
```

## Examples

```
merge_k_sorted([[1,4,5],[1,3,4],[2,6],[]])  ->  [1,1,2,3,4,4,5,6]
```

## Expected efficiency

O(N log k) where N = total elements.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
