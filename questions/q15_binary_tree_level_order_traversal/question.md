# Q15. Binary Tree Level Order Traversal

**Level:** Medium  |  **Topic:** Trees / BFS

## Problem

Given the root of a binary tree, return its node values level by level, left to right, as a list of lists.

## Signature

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None): ...

def level_order(root: TreeNode | None) -> list[list[int]]:
```

## Examples

```
Tree:      3
          / \
         9  20
           /  \
          15   7
level_order(root)  ->  [[3], [9, 20], [15, 7]]
```

## Expected efficiency

O(n).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
