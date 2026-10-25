"""Q12. Group Anagrams  (Medium | Hashing)

PROBLEM
Given a list of words, group the words that are anagrams of each other. The order of
groups and of words inside groups does not matter.

CONCEPT
Anagrams share the same multiset of letters, so a CANONICAL KEY (the sorted letters)
identifies the group. Turning 'which words belong together?' into 'bucket by key' is a
recurring hash-map pattern: normalise, then group.

defaultdict(list) removes the 'if key not in dict' boilerplate. The key must be
hashable: a list is not, so use tuple(sorted(w)) or ''.join(sorted(w)). For long words
with a small alphabet, a 26-count tuple key gives O(k) instead of O(k log k).

APPROACH
1. Create groups = defaultdict(list).
2. For each word compute key = tuple(sorted(word)).
3. Append the word to groups[key].
4. Return list(groups.values()).

COMPLEXITY
Time O(n * k log k) where k = longest word, Space O(n * k).

EDGE CASES
- Empty list.
- Empty string is a valid word (key ()).
- Case sensitivity - clarify with the interviewer.

FOLLOW-UPS
- Optimise the key with a 26-length count tuple.
- Check if two strings are anagrams using Counter.
"""
from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[tuple(sorted(w))].append(w)
    return list(groups.values())
