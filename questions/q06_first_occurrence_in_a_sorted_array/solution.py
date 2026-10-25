"""Q6. First Occurrence in a Sorted Array  (Easy | Binary Search)

PROBLEM
Given a sorted list that may contain duplicates, return the index of the first
occurrence of target, or -1 if it is absent.

CONCEPT
Binary search halves the search space each step, so it needs sorted (or otherwise
monotonic) data. The most bug-free formulation is the 'lower bound' template over a
half-open range [lo, hi): keep shrinking until lo == hi, where lo is the first index
with nums[lo] >= target.

Because we move hi = mid (not mid - 1) when nums[mid] >= target, we never skip over an
earlier duplicate. Afterwards we only need to verify that the element at lo really
equals the target. Python's bisect.bisect_left implements exactly this - mention it, but
be able to write it by hand.

APPROACH
1. lo = 0, hi = len(nums).
2. While lo < hi: mid = (lo + hi) // 2.
3. If nums[mid] < target: lo = mid + 1, else hi = mid.
4. Check bounds and equality, then return lo or -1.

COMPLEXITY
Time O(log n), Space O(1).

EDGE CASES
- Empty list.
- Target smaller than all / larger than all elements (lo == len(nums)).
- All elements equal to target.

FOLLOW-UPS
- Find the last occurrence (search for target+1 and subtract 1).
- Search in a rotated sorted array.
- Binary search on the answer (e.g. minimum capacity to ship packages).
"""


def first_occurrence(nums, target):
    lo, hi = 0, len(nums)  # search in [lo, hi)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo if lo < len(nums) and nums[lo] == target else -1
