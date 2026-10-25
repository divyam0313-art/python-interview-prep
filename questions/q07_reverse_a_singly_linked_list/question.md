# Q7. Reverse a Singly Linked List

**Level:** Easy  |  **Topic:** Linked List

## Problem

Given the head of a singly linked list, reverse it and return the new head. Do it iteratively, then explain the recursive version.

## Signature

```python
class ListNode:
    def __init__(self, val=0, next=None): ...

def reverse_list(head: ListNode | None) -> ListNode | None:
```

## Examples

```
1 -> 2 -> 3 -> 4   becomes   4 -> 3 -> 2 -> 1
```

## Expected efficiency

O(n) time, O(1) space.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
