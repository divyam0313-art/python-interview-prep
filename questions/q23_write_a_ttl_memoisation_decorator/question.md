# Q23. Write a TTL Memoisation Decorator

**Level:** Medium  |  **Topic:** Python Decorators / Closures

## Problem

Write a decorator `ttl_cache(ttl_seconds)` that caches a function's results per arguments, but treats an entry as expired after `ttl_seconds`. It must preserve the wrapped function's name/docstring and allow tests to inject a fake clock.

## Signature

```python
def ttl_cache(ttl_seconds, timer=time.monotonic):
```

## Examples

```
@ttl_cache(10)
def fetch(x): ...
fetch(2)   # computed
fetch(2)   # served from cache (within 10 s)
# after 11 s -> computed again
```

## Expected efficiency

Correct closure/decorator structure.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
