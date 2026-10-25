"""Q1. Two Sum  (Easy | Arrays / Hash Map)

PROBLEM
Given a list of integers nums and an integer target, return the indices of the two
numbers that add up to target. Exactly one valid pair exists; you may not use the same
element twice.

CONCEPT
A hash map (Python dict) gives O(1) average lookup. Instead of asking 'which other
element pairs with x?' by scanning the whole list (brute force O(n^2)), we remember
every number we have already seen together with its index.

For each new number x, the number we need is target - x (the complement). If the
complement is already in the dictionary, we are done. Otherwise we store x and move on.
This trades O(n) extra memory for a drop from O(n^2) to O(n) time - the classic 'time-
space trade-off'.

APPROACH
1. Create an empty dict seen mapping value -> index.
2. Loop with enumerate to get index and value.
3. If target - x is in seen, return [seen[target - x], i].
4. Otherwise store seen[x] = i.

COMPLEXITY
Time O(n), Space O(n).

EDGE CASES
- Duplicates such as [3, 3] work because we check before we insert.
- Negative numbers and zero need no special handling.
- No solution -> returns an empty list (agree this with the interviewer).

FOLLOW-UPS
- What if the array is sorted? (Two pointers, O(1) space.)
- What if several pairs exist and you must return all of them?
- How would you do it if the data does not fit in memory?
"""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
