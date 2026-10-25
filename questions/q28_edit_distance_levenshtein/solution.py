"""Q28. Edit Distance (Levenshtein)  (Hard | Dynamic Programming (2-D))

PROBLEM
Given two words, return the minimum number of single-character operations (insert,
delete, replace) needed to convert a into b.

CONCEPT
dp[i][j] = minimum edits to turn the first i characters of a into the first j characters
of b. Base cases: converting to/from an empty string costs the length of the other
string (dp[i][0] = i, dp[0][j] = j).

If the current characters match, the cost is dp[i-1][j-1] (no operation needed).
Otherwise take 1 + the cheapest of: replace (dp[i-1][j-1]), delete from a (dp[i-1][j]),
insert into a (dp[i][j-1]). It powers spell checkers, fuzzy search and DNA alignment.

APPROACH
1. prev = [0, 1, ..., len(b)] (row for the empty prefix of a).
2. For each i start cur = [i, ...].
3. Fill each j with the match / replace-delete-insert rule.
4. Roll prev = cur; the answer is prev[-1].

COMPLEXITY
Time O(m x n), Space O(n).

EDGE CASES
- One or both strings empty.
- Identical strings -> 0.
- Very long strings: O(m x n) memory matters, hence the rolling row.

FOLLOW-UPS
- Reconstruct the actual operations (keep the full table).
- Add a transposition (Damerau-Levenshtein).
- One edit distance (O(n) special case).
"""


def edit_distance(a, b):
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j - 1],  # replace
                                 prev[j],      # delete
                                 cur[j - 1])   # insert
        prev = cur
    return prev[-1]
