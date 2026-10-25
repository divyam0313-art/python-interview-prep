"""Q30. Merge K Sorted Lists  (Hard | Heap / K-way Merge)

PROBLEM
Given k sorted lists, merge them into one sorted list efficiently. Discuss what changes
if the lists are huge or streamed from disk.

CONCEPT
Comparing the front of all k lists each time costs O(k) per output element (O(N x k)). A
MIN-HEAP of size k holding the current front element of each list gives the global
minimum in O(log k). Pop it, then push the next element from the same list.

Python's heapq is a min-heap on tuples. Store (value, list_index, element_index) - the
index acts as a tie-breaker so Python never has to compare two non-comparable payloads
(for example linked-list nodes) when values are equal. In production use
heapq.merge(*lists), which is a lazy generator and works with iterators/files too.

APPROACH
1. Push (first_value, i, 0) for each non-empty list; heapify.
2. Pop the smallest, append its value to the output.
3. Push the next element of that list if it exists.
4. Repeat until the heap is empty.

COMPLEXITY
Time O(N log k), Space O(k) besides the output.

EDGE CASES
- Empty lists inside the input.
- k = 0 or k = 1.
- Duplicate values across lists (tie-breaker index).

FOLLOW-UPS
- Same problem on linked lists (LeetCode 23).
- Divide-and-conquer merging (pairwise merge, also O(N log k)).
- External sort of a file bigger than RAM.
"""
import heapq


def merge_k_sorted(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    out = []
    while heap:
        value, i, j = heapq.heappop(heap)
        out.append(value)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out
