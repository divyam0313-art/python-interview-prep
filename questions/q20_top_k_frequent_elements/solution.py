"""Q20. Top K Frequent Elements  (Medium | Heap / Counter)

PROBLEM
Return the k most frequent elements of nums (any order). The algorithm should be better
than sorting everything when k is small.

CONCEPT
Step 1: count frequencies with collections.Counter (O(n)). Step 2: choose the top k.
Sorting all distinct values costs O(m log m); a heap of size k costs O(m log k).
heapq.nlargest(k, iterable, key=...) does exactly that.

A linear-time alternative is bucket sort: since a frequency can be at most n, create n+1
buckets indexed by frequency and read from the highest bucket down. Mention both and
explain the trade-off - heaps are simpler, buckets are O(n).

APPROACH
1. freq = Counter(nums).
2. Return heapq.nlargest(k, freq.keys(), key=freq.get).

COMPLEXITY
Time O(n + m log k) with m distinct values, Space O(m).

EDGE CASES
- k equals number of distinct values.
- Ties - any order is accepted unless stated.
- Negative numbers work (they are only dict keys).

FOLLOW-UPS
- Top K frequent words with alphabetical tie-break (heap with tuples).
- Streaming data: keep a min-heap of size k.
- K closest points to origin.
"""
import heapq
from collections import Counter


def top_k_frequent(nums, k):
    freq = Counter(nums)
    return heapq.nlargest(k, freq.keys(), key=freq.get)
