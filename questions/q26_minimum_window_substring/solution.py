"""Q26. Minimum Window Substring  (Hard | Sliding Window (variable))

PROBLEM
Given strings s and t, return the smallest substring of s that contains every character
of t (including duplicates). Return an empty string if no such window exists.

CONCEPT
This is the template for hard sliding-window problems: EXPAND the right edge until the
window is valid, then SHRINK from the left as long as it stays valid, recording the best
window. Both pointers only move forward, so the total work is linear.

Bookkeeping: need[c] is how many more of character c we still require (negative means
surplus). missing counts how many required characters are still uncovered, so validity
is the O(1) test missing == 0 instead of comparing dictionaries every step.

APPROACH
1. Build need = Counter(t), missing = len(t).
2. Move right: if need[ch] > 0 a required character is covered -> missing -= 1; always
need[ch] -= 1.
3. When missing == 0 slide left while need[s[left]] < 0 (surplus characters).
4. Record the window, then evict s[left] to break validity and continue.

COMPLEXITY
Time O(n), Space O(alphabet).

EDGE CASES
- t longer than s.
- t has duplicate characters ('aa').
- Whole string is the answer.

FOLLOW-UPS
- Permutation in string (fixed-size window).
- Find all anagrams in a string.
- Smallest range covering elements from K lists.
"""
from collections import Counter


def min_window(s, t):
    if not t or len(t) > len(s):
        return ""
    need = Counter(t)
    missing = len(t)  # characters of t still to be covered
    best_start, best_end = 0, float('inf')
    left = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        if missing == 0:
            while need[s[left]] < 0:  # drop surplus characters on the left
                need[s[left]] += 1
                left += 1
            if right - left < best_end - best_start:
                best_start, best_end = left, right
            need[s[left]] += 1  # break the window to look for the next one
            missing += 1
            left += 1
    return "" if best_end == float('inf') else s[best_start:best_end + 1]
