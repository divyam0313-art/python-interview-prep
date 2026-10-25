"""Q4. Remove Duplicates from a Sorted Array (in place)  (Easy | Two Pointers (read / write))

PROBLEM
Given a sorted list nums, remove duplicates in place so each value appears once. Return
the new length k; the first k elements of nums must hold the unique values in order. Do
not allocate another list.

CONCEPT
This is the 'slow / fast' (read / write) pointer pattern. The fast pointer read scans
every element; the slow pointer write marks where the next unique value must be placed.

Because the input is sorted, duplicates are adjacent, so comparing nums[read] with the
last written value nums[write - 1] is enough to detect a new value. The same pattern
solves 'remove element', 'move zeroes' and 'partition' problems.

APPROACH
1. Handle the empty list.
2. Start write = 1 (the first element is always unique).
3. For read in 1..n-1: if nums[read] differs from nums[write-1], copy it to nums[write]
and increment write.
4. Return write.

COMPLEXITY
Time O(n), Space O(1).

EDGE CASES
- Empty list -> 0.
- All elements equal -> 1.
- No duplicates -> pointers move together, nothing changes.

FOLLOW-UPS
- Allow each value at most twice (compare with nums[write-2]).
- What if the list is not sorted? (Use a set; O(n) space.)
"""


def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write
