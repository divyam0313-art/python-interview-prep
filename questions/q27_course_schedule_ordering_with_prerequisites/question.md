# Q27. Course Schedule (Ordering with Prerequisites)

**Level:** Hard  |  **Topic:** Graphs / Topological Sort

## Problem

There are `num_courses` courses labelled 0..n-1. Each pair `[a, b]` in `prerequisites` means you must take b before a. Return a valid order to finish all courses, or an empty list if it is impossible (a cycle exists).

## Signature

```python
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
```

## Examples

```
find_order(4, [[1,0],[2,0],[3,1],[3,2]])  ->  [0, 1, 2, 3]  (or [0,2,1,3])
find_order(2, [[1,0],[0,1]])  ->  []
```

## Expected efficiency

O(V + E).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
