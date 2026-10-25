"""Q14. Merge Overlapping Intervals  (Medium | Sorting / Intervals)

PROBLEM
Given a list of intervals [start, end], merge all overlapping intervals and return the
non-overlapping result.

CONCEPT
Interval problems become simple once the intervals are SORTED BY START. Then any overlap
can only be with the most recently merged interval, so one linear pass with a 'last
merged' reference is enough.

Overlap test: the new interval's start <= the last merged end. In that case extend the
end with max(...) (the new interval might be fully contained). Otherwise it starts a new
group. The sort dominates the cost.

APPROACH
1. Sort by start (sorted(intervals) sorts lists lexicographically).
2. For each (start, end): if merged is non-empty and start <= merged[-1][1], extend with
max.
3. Else append a new interval.

COMPLEXITY
Time O(n log n), Space O(n).

EDGE CASES
- Empty input.
- Contained interval [1,10] and [2,3] -> need max().
- Touching intervals - confirm whether [1,4],[4,5] merge.

FOLLOW-UPS
- Insert a new interval into a sorted list.
- Minimum meeting rooms (heap or sweep line).
- Non-overlapping intervals - minimum removals.
"""


def merge_intervals(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
