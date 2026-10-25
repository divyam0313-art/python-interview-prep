# Q22. Design an LRU Cache

**Level:** Medium  |  **Topic:** Design / Data Structures

## Problem

Design a Least Recently Used cache with `get(key)` and `put(key, value)` both in O(1). When capacity is exceeded, evict the least recently used entry. `get` of a missing key returns -1. First solve it with the standard library, then implement it from scratch.

## Signature

```python
class LRUCache:
    def __init__(self, capacity: int): ...
    def get(self, key: int) -> int: ...
    def put(self, key: int, value: int) -> None: ...
```

## Examples

```
cache = LRUCache(2)
cache.put(1, 1); cache.put(2, 2)
cache.get(1)   -> 1
cache.put(3, 3)   # evicts key 2
cache.get(2)   -> -1
```

## Expected efficiency

O(1) for both operations.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
