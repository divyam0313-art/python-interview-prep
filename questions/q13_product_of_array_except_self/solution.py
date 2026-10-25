"""Q13. Product of Array Except Self  (Medium | Prefix / Suffix Arrays)

PROBLEM
Return a list out where out[i] is the product of all elements of nums except nums[i]. Do
not use division and run in O(n).

CONCEPT
Product of everything except i = (product of everything LEFT of i) x (product of
everything RIGHT of i). Prefix/suffix accumulation precomputes such running aggregates
so each answer is O(1).

To save memory, store left products directly in the output list, then make a second
right-to-left pass that multiplies in a running suffix product. Division is avoided
because it fails when the array contains zeros.

APPROACH
1. Pass 1 (left to right): out[i] = product of nums[0..i-1].
2. Pass 2 (right to left): multiply out[i] by the running product of nums[i+1..].
3. Return out.

COMPLEXITY
Time O(n), Space O(1) extra.

EDGE CASES
- One zero -> only that position is non-zero.
- Two or more zeros -> all zeros.
- Negative numbers.

FOLLOW-UPS
- Same idea for sums / prefix-sum range queries.
- Solve with division and handle zeros explicitly.
"""


def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    return out
