"""Q29. Longest Increasing Subsequence in O(n log n)  (Hard | DP + Binary Search)

PROBLEM
Return the length of the longest strictly increasing subsequence of nums. Give the
O(n^2) DP idea first, then the O(n log n) solution.

CONCEPT
Simple DP: dp[i] = LIS ending at i = 1 + max(dp[j]) for j < i with nums[j] < nums[i].
That is O(n^2) and always acceptable as a first answer.

The optimisation ('patience sorting'): keep tails, where tails[k] is the SMALLEST
possible last element of an increasing subsequence of length k+1. tails is always
sorted, so for each new number we binary-search (bisect_left) the first tail >= x and
overwrite it: a smaller tail keeps future options open. If x is bigger than every tail,
append - the LIS grows. Note: tails is NOT the subsequence itself, only its length is
meaningful.

APPROACH
1. tails = [].
2. For each x: i = bisect_left(tails, x).
3. If i == len(tails) append x, else tails[i] = x.
4. Answer is len(tails).

COMPLEXITY
Time O(n log n), Space O(n).

EDGE CASES
- Empty list -> 0.
- Equal values: bisect_left makes the subsequence STRICTLY increasing; use bisect_right
for non-decreasing.
- Already sorted / reverse sorted.

FOLLOW-UPS
- Reconstruct the subsequence (store predecessors).
- Russian doll envelopes (sort + LIS).
- Number of LIS (DP with counts).
"""
from bisect import bisect_left


def length_of_lis(nums):
    tails = []  # tails[i] = smallest tail of any increasing subsequence of length i+1
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
