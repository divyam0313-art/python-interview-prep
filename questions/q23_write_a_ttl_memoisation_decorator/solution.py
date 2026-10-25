"""Q23. Write a TTL Memoisation Decorator  (Medium | Python Decorators / Closures)

PROBLEM
Write a decorator ttl_cache(ttl_seconds) that caches a function's results per arguments,
but treats an entry as expired after ttl_seconds. It must preserve the wrapped
function's name/docstring and allow tests to inject a fake clock.

CONCEPT
A decorator with arguments is a THREE-level structure: ttl_cache(args) returns
decorator(fn) which returns wrapper(*args, **kwargs). Each level closes over the
variables of the one above - the cache dict lives in the closure and is private per
decorated function.

functools.wraps(fn) copies __name__, __doc__, etc. onto the wrapper (otherwise debugging
and introspection break). Use time.monotonic() for measuring durations because
time.time() can jump when the system clock changes. Passing timer as a parameter is
dependency injection that makes the code deterministic to unit-test.

APPROACH
1. Outer function receives the configuration (TTL, timer).
2. decorator(fn) creates the private cache dict.
3. Build a hashable key from args and sorted kwargs.
4. If a fresh entry exists return it, else call fn, store (value, timestamp).
5. Expose cache_clear for tests/ops.

COMPLEXITY
O(1) average per call; memory grows with distinct argument sets.

EDGE CASES
- Unhashable arguments (lists) raise TypeError when building the key.
- Cache stampede: many threads miss at once.
- Entries are never evicted, only ignored - memory leak over time.

FOLLOW-UPS
- Add a lock for thread safety and a max size (combine with LRU).
- Support async functions (await fn(...), store the result).
- Cache exceptions? Negative caching?
"""
import functools
import time


def ttl_cache(ttl_seconds, timer=time.monotonic):
    def decorator(fn):
        cache = {}

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = timer()
            hit = cache.get(key)
            if hit is not None and now - hit[1] < ttl_seconds:
                return hit[0]
            value = fn(*args, **kwargs)
            cache[key] = (value, now)
            return value

        wrapper.cache_clear = cache.clear
        return wrapper

    return decorator
