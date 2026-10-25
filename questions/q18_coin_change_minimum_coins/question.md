# Q18. Coin Change (Minimum Coins)

**Level:** Medium  |  **Topic:** Dynamic Programming (unbounded knapsack)

## Problem

Given coin denominations `coins` (unlimited supply of each) and a target `amount`, return the minimum number of coins needed to make that amount, or -1 if it is impossible.

## Signature

```python
def coin_change(coins: list[int], amount: int) -> int:
```

## Examples

```
coin_change([1,2,5], 11)  ->  3   # 5+5+1
coin_change([2], 3)        ->  -1
```

## Expected efficiency

O(amount x len(coins)).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
