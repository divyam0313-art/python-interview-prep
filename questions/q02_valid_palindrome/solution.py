"""Q2. Valid Palindrome  (Easy | Two Pointers / Strings)

PROBLEM
Given a string s, return True if it reads the same forwards and backwards after ignoring
case and every non-alphanumeric character.

CONCEPT
The two-pointer technique places one pointer at each end of a sequence and moves them
toward each other. It is the go-to pattern whenever the problem is symmetric or the data
is sorted.

The naive answer cleaned = ''.join(c.lower() for c in s if c.isalnum()); return cleaned
== cleaned[::-1] is correct and perfectly Pythonic, but uses O(n) extra memory. The
pointer version does the comparison in place and shows you understand the underlying
technique.

APPROACH
1. Set left = 0, right = len(s) - 1.
2. Advance left while the character is not alphanumeric; retreat right likewise.
3. Compare the lowercase characters; if they differ return False.
4. Move both pointers inward; if they cross, return True.

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- Empty string or only punctuation -> True.
- Inner while loops must re-check left < right to avoid index errors.
- Unicode: str.isalnum handles letters beyond ASCII.

FOLLOW-UPS
- Valid Palindrome II: you may delete at most one character.
- Longest palindromic substring (expand around centre, O(n^2)).
"""


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
