"""Q25. Trapping Rain Water  (Hard | Two Pointers / Arrays)

PROBLEM
Given non-negative integers representing an elevation map (each bar has width 1),
compute how much water it can trap after raining.

CONCEPT
Water above a bar = min(tallest bar to its left, tallest bar to its right) - its own
height. Precomputing left-max and right-max arrays gives an O(n) time, O(n) space
solution (a perfectly good first answer).

The O(1)-space refinement uses two pointers: whichever side currently has the SMALLER
boundary is the side whose water level is already decided, because the other side has at
least as tall a wall. So we process that side, maintaining only its running maximum, and
move inward.

APPROACH
1. Pointers at both ends; left_max = right_max = 0.
2. If height[left] < height[right]: update left_max, add left_max - height[left], move
left.
3. Else do the symmetric thing on the right.
4. Stop when pointers meet.

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- Fewer than 3 bars -> 0.
- Monotonic increasing/decreasing -> 0.
- Flat plateau.

FOLLOW-UPS
- Trapping Rain Water II (2-D, heap/Dijkstra-style).
- Solve with a monotonic stack.
- Largest rectangle in histogram (monotonic stack).
"""


def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water
