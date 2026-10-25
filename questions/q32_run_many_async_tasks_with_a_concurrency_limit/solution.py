"""Q32. Run Many Async Tasks with a Concurrency Limit  (Hard | Concurrency / asyncio)

PROBLEM
Write async def run_bounded(factories, limit) that runs the coroutine factories
concurrently, never more than limit at the same time, returns results in the SAME ORDER
as the input, and does not let one failure cancel the others (return the exception
object in its slot).

CONCEPT
asyncio is cooperative, single-threaded concurrency: it shines for I/O-bound work (HTTP
calls, DB queries). Launching 10,000 requests at once can exhaust sockets or get you
rate-limited, so we cap concurrency with an asyncio.Semaphore.

asyncio.gather(*coros) runs awaitables concurrently and returns results in input order.
With return_exceptions=True an exception is returned as a value instead of cancelling
the rest. We pass FACTORIES (callables) rather than ready-made coroutine objects so that
no work starts until it has acquired the semaphore. For CPU-bound work asyncio does not
help: use multiprocessing / ProcessPoolExecutor; for blocking libraries use
run_in_executor.

APPROACH
1. Create Semaphore(limit) inside the running loop.
2. Wrap each factory: async with semaphore: return await factory().
3. gather all wrappers with return_exceptions=True.
4. Results come back ordered; check with isinstance(r, Exception).

COMPLEXITY
Time depends on the tasks; at most limit run concurrently; Space O(n) for results.

EDGE CASES
- limit larger than number of tasks.
- limit <= 0 would deadlock - validate it.
- Cancellation: wrap in try/except asyncio.CancelledError and re-raise.

FOLLOW-UPS
- Python 3.11+: asyncio.TaskGroup and its different failure semantics.
- Add per-task timeouts with asyncio.timeout.
- GIL: threads vs processes vs asyncio - when do you choose each?
"""
import asyncio


async def run_bounded(factories, limit):
    semaphore = asyncio.Semaphore(limit)

    async def run(factory):
        async with semaphore:
            return await factory()

    return await asyncio.gather(*(run(f) for f in factories),
                                return_exceptions=True)
