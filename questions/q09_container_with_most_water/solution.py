"""Q9. Container With Most Water  (Medium | Two Pointers (greedy))

PROBLEM
Given a list height where each value is the height of a vertical line at that index,
pick two lines that, together with the x-axis, form a container holding the most water.
Return the maximum area.

CONCEPT
Brute force checks all pairs: O(n^2). The two-pointer insight: start with the widest
container (first and last line). Area = min(h[l], h[r]) * (r - l). The shorter line
limits the height, so moving the TALLER pointer inward can only shrink the width without
any chance of a taller limit - it can never help.

Therefore we always move the pointer at the shorter line, hoping to find a taller one.
Each step discards a whole set of pairs that cannot beat the current best, which is why
a single pass suffices. Being able to justify 'why move the shorter side' is what
interviewers look for.

APPROACH
1. Pointers at both ends, best = 0.
2. Compute area, update best.
3. Move the pointer with the smaller height inward.
4. Stop when the pointers meet.

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- Two elements.
- Zero heights.
- Equal heights - moving either is fine.

FOLLOW-UPS
- Trapping rain water (Q25) - same family, harder.
- Prove the greedy choice correct.
"""


def max_area(height):
    left, right, best = 0, len(height) - 1, 0
    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
