# Q3. Valid Parentheses

**Level:** Easy  |  **Topic:** Stack

## Problem

Given a string containing only `()[]{}`, determine whether the brackets are balanced: every opener is closed by the same type, in the correct order.

## Signature

```python
def is_valid_parentheses(s: str) -> bool:
```

## Examples

```
is_valid_parentheses("()[]{}")  ->  True
is_valid_parentheses("(]")      ->  False
is_valid_parentheses("([)]")    ->  False
```

## Expected efficiency

O(n).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
