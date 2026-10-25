# Q16. Number of Islands

**Level:** Medium  |  **Topic:** Graphs / Grid DFS

## Problem

Given a 2-D grid of '1' (land) and '0' (water), count the islands. An island is a group of land cells connected horizontally or vertically.

## Signature

```python
def num_islands(grid: list[str] | list[list[str]]) -> int:
```

## Examples

```
grid = ["11000",
        "11000",
        "00100",
        "00011"]
num_islands(grid)  ->  3
```

## Expected efficiency

O(rows x cols).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
