# Q4. Remove Duplicates from a Sorted Array (in place)

**Level:** Easy  |  **Topic:** Two Pointers (read / write)

## Problem

Given a sorted list `nums`, remove duplicates in place so each value appears once. Return the new length k; the first k elements of `nums` must hold the unique values in order. Do not allocate another list.

## Signature

```python
def remove_duplicates(nums: list[int]) -> int:
```

## Examples

```
nums = [0,0,1,1,1,2,2,3,3,4]
remove_duplicates(nums)  ->  5   # nums[:5] == [0,1,2,3,4]
```

## Expected efficiency

O(n) time, O(1) space.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
