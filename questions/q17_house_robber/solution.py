"""Q17. House Robber  (Medium | Dynamic Programming (1-D))

PROBLEM
Each house holds some money, but you cannot rob two adjacent houses. Given nums (money
per house in a row), return the maximum you can rob.

CONCEPT
Dynamic programming = break the problem into overlapping sub-problems, define a STATE,
write a RECURRENCE and avoid recomputation. Here state i = best total using the first i
houses. Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i]) (skip house i, or rob it and
skip i-1).

Since dp[i] only depends on the previous two values, we keep two variables instead of an
array (space optimisation). A good interview flow: (1) brute-force recursion, (2) add
memoisation (functools.lru_cache), (3) convert to bottom-up table, (4) compress space.

APPROACH
1. take = best total if we rob the current house; skip = best if we do not.
2. For each x: new take = old skip + x; new skip = max(old take, old skip).
3. Tuple assignment updates both from the OLD values at once.
4. Answer is max(take, skip).

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- Empty list -> 0.
- Single house.
- Two houses -> the larger one.

FOLLOW-UPS
- House Robber II: houses in a circle.
- House Robber III: houses form a binary tree.
- Climbing stairs / min cost climbing stairs (same recurrence family).
"""


def rob(nums):
    take, skip = 0, 0  # best total if we rob / don't rob the current house
    for x in nums:
        take, skip = skip + x, max(take, skip)
    return max(take, skip)
