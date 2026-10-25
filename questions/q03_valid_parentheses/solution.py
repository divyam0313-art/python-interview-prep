"""Q3. Valid Parentheses  (Easy | Stack)

PROBLEM
Given a string containing only ()[]{}, determine whether the brackets are balanced:
every opener is closed by the same type, in the correct order.

CONCEPT
A stack is a last-in-first-out structure. Nested structures (brackets, HTML tags,
function calls, expression parsing) are naturally LIFO: the most recently opened bracket
must be the first one closed.

In Python a plain list is the stack: append pushes and pop pops, both O(1) amortised.
(Use collections.deque for a queue, never list.pop(0) which is O(n).)

APPROACH
1. Map each closing bracket to its opener.
2. Push every opener onto the stack.
3. On a closer: the stack must be non-empty and its top must match, otherwise return
False.
4. At the end the stack must be empty (no unclosed openers).

COMPLEXITY
Time O(n), Space O(n).

EDGE CASES
- Only closers, e.g. ']' -> empty stack, return False.
- Only openers, e.g. '((' -> stack not empty at the end.
- Empty string -> True.

FOLLOW-UPS
- Return the index of the first invalid bracket.
- Longest valid parentheses substring (DP or stack of indices).
"""


def is_valid_parentheses(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
