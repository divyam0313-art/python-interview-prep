"""Q24. Longest Common Subsequence  (Medium | Dynamic Programming (2-D))

PROBLEM
Given two strings a and b, return the length of their longest common subsequence
(characters in the same order, not necessarily contiguous).

CONCEPT
Two-sequence problems almost always map to a 2-D DP table where dp[i][j] answers the
question for the prefixes a[:i] and b[:j]. If the last characters match, we extend the
best answer of the shorter prefixes: dp[i-1][j-1] + 1. Otherwise we drop one character
from either string: max(dp[i-1][j], dp[i][j-1]).

Each row depends only on the previous row, so two 1-D lists are enough: space drops from
O(m x n) to O(n). Keep the full table if you must reconstruct the actual subsequence by
walking back from dp[m][n].

APPROACH
1. prev = row of zeros (empty prefix of a).
2. For each char of a build cur left to right.
3. Match -> prev[j-1] + 1; mismatch -> max(prev[j], cur[j-1]).
4. Swap rows; the answer is the last cell.

COMPLEXITY
Time O(m x n), Space O(n).

EDGE CASES
- Empty strings -> 0.
- Identical strings -> length of the string.
- Subsequence vs substring - clarify.

FOLLOW-UPS
- Print the subsequence.
- Longest common substring (reset to 0 on mismatch).
- Shortest common supersequence; minimum deletions to make strings equal.
"""


def lcs_length(a, b):
    prev = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        cur = [0] * (len(b) + 1)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]
