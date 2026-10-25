"""Q8. Flatten a Nested List Lazily  (Easy | Python Idioms / Generators)

PROBLEM
Write a generator flatten(items) that yields every non-list element of an arbitrarily
nested structure of lists/tuples, in order. Strings must be treated as single values,
not iterated.

CONCEPT
A generator function uses yield to produce values one at a time, keeping its local state
between calls. It uses O(1) memory for the output and is the right tool for pipelines
over large or unbounded data.

yield from other_generator delegates to a sub-generator and forwards all its values -
ideal for recursion. We check isinstance(x, (list, tuple)) instead of 'is iterable'
because strings are iterable and would recurse forever (a one-character string contains
itself).

APPROACH
1. Loop over the items.
2. If the item is a list/tuple, yield from flatten(item).
3. Otherwise yield item.

COMPLEXITY
Time O(total elements), Space O(depth) for the recursion stack.

EDGE CASES
- Empty nested lists yield nothing.
- Strings/bytes must not be expanded.
- Depth beyond ~1000 raises RecursionError - see follow-up.

FOLLOW-UPS
- Rewrite it iteratively with an explicit stack to support unlimited depth.
- How would you support any iterable except str/bytes (collections.abc.Iterable)?
"""


def flatten(items):
    for x in items:
        if isinstance(x, (list, tuple)):
            yield from flatten(x)
        else:
            yield x
