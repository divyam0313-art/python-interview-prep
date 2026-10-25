"""Q11. Longest Substring Without Repeating Characters  (Medium | Sliding Window)

PROBLEM
Given a string s, return the length of the longest substring that contains no repeated
character.

CONCEPT
Sliding window keeps a window [start, i] that always satisfies the constraint (no
duplicates) and grows/shrinks as we scan. Each character enters and leaves the window at
most once, so the whole scan is linear even though there is a nested-looking shrink
step.

Storing the LAST INDEX of every character lets us jump start directly past the previous
occurrence instead of moving it one step at a time. The condition last_seen[ch] >= start
is essential: an old occurrence that is already outside the window must be ignored (the
'abba' trap).

APPROACH
1. Keep last_seen dict and start = 0.
2. For each index i and char ch: if ch was seen at or after start, set start =
last_seen[ch] + 1.
3. Record last_seen[ch] = i.
4. Update best = max(best, i - start + 1).

COMPLEXITY
Time O(n), Space O(min(n, alphabet)).

EDGE CASES
- Empty string -> 0.
- All same characters -> 1.
- 'abba': when reading the final 'a', its old index is before start, so start must not
move backwards.

FOLLOW-UPS
- At most K distinct characters.
- Return the substring itself, not the length.
- Longest repeating character replacement.
"""


def length_of_longest_substring(s):
    last_seen = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best
