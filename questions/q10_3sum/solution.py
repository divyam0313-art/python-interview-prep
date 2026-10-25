"""Q10. 3Sum  (Medium | Sorting + Two Pointers)

PROBLEM
Return all unique triplets [a, b, c] in nums such that a + b + c == 0. The result must
not contain duplicate triplets.

CONCEPT
Reduce a hard problem to an easier one: fix the first number a, then the rest is a
sorted 'two-sum' that two pointers solve in O(n). Total O(n log n) sort + O(n^2) =
O(n^2), far better than O(n^3) brute force.

Sorting is also what makes de-duplication easy: equal numbers become adjacent, so we
skip an anchor equal to the previous anchor, and after recording a triplet we skip
repeated values of the left pointer. Using a set of tuples is an alternative but costs
extra memory and hides the technique.

APPROACH
1. Sort a copy of the input.
2. For each index i: stop if nums[i] > 0 (all later values are positive, the sum cannot
be zero).
3. Skip i if it equals nums[i-1].
4. Use left = i+1, right = n-1. If total < 0 move left; if > 0 move right.
5. When total == 0 record it, move left, and skip duplicates.

COMPLEXITY
Time O(n^2), Space O(1) extra (ignoring output and the sorted copy).

EDGE CASES
- Fewer than 3 elements -> [].
- Many zeros -> exactly one [0,0,0].
- Duplicate handling is the usual source of bugs - test [-2,0,0,2,2].

FOLLOW-UPS
- 3Sum Closest.
- 4Sum / kSum generalisation (recursion over k).
- Count triplets instead of listing them.
"""


def three_sum(nums):
    nums = sorted(nums)
    result = []
    for i, a in enumerate(nums):
        if a > 0:
            break
        if i > 0 and a == nums[i - 1]:
            continue  # skip duplicate anchors
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = a + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([a, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return result
