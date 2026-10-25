# Q13. Product of Array Except Self

**Level:** Medium  |  **Topic:** Prefix / Suffix Arrays

## Problem

Return a list `out` where `out[i]` is the product of all elements of `nums` except `nums[i]`. Do not use division and run in O(n).

## Signature

```python
def product_except_self(nums: list[int]) -> list[int]:
```

## Examples

```
product_except_self([1,2,3,4])  ->  [24,12,8,6]
product_except_self([1,0,3,4])  ->  [0,12,0,0]
```

## Expected efficiency

O(n) time, O(1) extra space besides the output.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
