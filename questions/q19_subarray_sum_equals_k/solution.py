"""Q19. Subarray Sum Equals K  (Medium | Prefix Sum + Hash Map)

PROBLEM
Count the contiguous subarrays of nums whose sum equals k. The list may contain negative
numbers.

CONCEPT
Let prefix[i] be the sum of the first i elements. The sum of a subarray (j, i] equals
prefix[i] - prefix[j]. We want that to be k, i.e. we need an EARLIER prefix equal to
prefix[i] - k. So while scanning, keep a Counter of how many times each prefix sum has
occurred.

A sliding window does NOT work here because negative numbers break the 'grow window
increases sum' monotonicity. The seed Counter({0: 1}) represents the empty prefix so
subarrays starting at index 0 are counted.

APPROACH
1. seen = Counter({0: 1}), prefix = 0, count = 0.
2. For each x: prefix += x.
3. count += seen[prefix - k].
4. seen[prefix] += 1.

COMPLEXITY
Time O(n), Space O(n).

EDGE CASES
- Negative numbers and zeros (many overlapping answers).
- k = 0.
- Forgetting the {0: 1} seed is the #1 bug.

FOLLOW-UPS
- Longest subarray with sum k (store first index instead of count).
- Continuous subarray sum divisible by k (store prefix mod k).
- Count subarrays with equal 0s and 1s.
"""
from collections import Counter


def subarray_sum(nums, k):
    count = prefix = 0
    seen = Counter({0: 1})  # prefix sum -> how many times seen
    for x in nums:
        prefix += x
        count += seen[prefix - k]
        seen[prefix] += 1
    return count
