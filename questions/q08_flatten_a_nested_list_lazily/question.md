# Q8. Flatten a Nested List Lazily

**Level:** Easy  |  **Topic:** Python Idioms / Generators

## Problem

Write a generator `flatten(items)` that yields every non-list element of an arbitrarily nested structure of lists/tuples, in order. Strings must be treated as single values, not iterated.

## Signature

```python
def flatten(items):  # generator
```

## Examples

```
list(flatten([1, [2, [3, [4]], 5], (6, 7), "ab"]))  ->  [1, 2, 3, 4, 5, 6, 7, "ab"]
```

## Expected efficiency

Lazy evaluation - do not build the whole result list first.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
