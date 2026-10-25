"""Q7. Reverse a Singly Linked List  (Easy | Linked List)

PROBLEM
Given the head of a singly linked list, reverse it and return the new head. Do it
iteratively, then explain the recursive version.

CONCEPT
Linked-list problems are about pointer manipulation. To reverse, we walk the list once
and flip each next pointer so it points to the previous node. We need three references:
prev (already reversed part), head (current node) and nxt (saved so we do not lose the
rest of the list when we overwrite head.next).

The classic bug is overwriting head.next before saving it. The recursive solution is
shorter but uses O(n) call stack - Python's default recursion limit (about 1000) makes
it unsafe for long lists.

APPROACH
1. prev = None.
2. While head: save nxt = head.next.
3. Point head.next = prev.
4. Advance: prev = head, head = nxt.
5. Return prev (the new head).

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- Empty list (head is None) -> returns None.
- Single node.
- Very long list: iterative avoids RecursionError.

FOLLOW-UPS
- Reverse only between positions m and n.
- Detect a cycle (Floyd's slow/fast pointers).
- Merge two sorted linked lists.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
