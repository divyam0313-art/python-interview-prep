"""Q5. Maximum Subarray  (Easy | Dynamic Programming (Kadane))

PROBLEM
Given a list of integers (positive and negative), find the contiguous subarray with the
largest sum and return that sum.

CONCEPT
Kadane's algorithm is the simplest dynamic-programming idea: the best subarray ending at
position i is either the element alone, or the best subarray ending at i-1 extended by
this element. In symbols: best_ending_here = max(x, best_ending_here + x).

If the running sum becomes a burden (negative), we drop it and restart at the current
element. The global answer is the maximum of all 'ending here' values. We only need the
previous value, so no DP table is required.

APPROACH
1. Initialise best and current with the first element (not 0 - the array may be all
negative).
2. For every remaining x: current = max(x, current + x).
3. Update best = max(best, current).
4. Return best.

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- All-negative array: answer is the largest single element (this is why we do not start
at 0).
- Single element.
- Large values: Python ints do not overflow.

FOLLOW-UPS
- Also return the start and end indices.
- Maximum circular subarray.
- Maximum product subarray (track both max and min).
"""


def max_subarray(nums):
    best = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)  # extend the run or restart at x
        best = max(best, current)
    return best
