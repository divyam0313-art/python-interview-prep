# Q32. Run Many Async Tasks with a Concurrency Limit

**Level:** Hard  |  **Topic:** Concurrency / asyncio

## Problem

Write `async def run_bounded(factories, limit)` that runs the coroutine factories concurrently, never more than `limit` at the same time, returns results in the SAME ORDER as the input, and does not let one failure cancel the others (return the exception object in its slot).

## Signature

```python
async def run_bounded(factories, limit):
```

## Examples

```
await run_bounded([lambda: fetch(u) for u in urls], limit=5)
# -> [result0, result1, ValueError(...), result3, ...]
```

## Expected efficiency

Correct use of asyncio primitives.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
