"""Q15. Binary Tree Level Order Traversal  (Medium | Trees / BFS)

PROBLEM
Given the root of a binary tree, return its node values level by level, left to right,
as a list of lists.

CONCEPT
Breadth-first search (BFS) explores a graph/tree layer by layer using a QUEUE. Depth-
first search (DFS) uses a stack or recursion. Choose BFS whenever the question is about
levels, shortest path in an unweighted graph, or 'minimum steps'.

The trick for level grouping is to take len(queue) at the start of each round: exactly
that many nodes belong to the current level. Always use collections.deque - list.pop(0)
is O(n) and turns the algorithm into O(n^2).

APPROACH
1. Return [] for an empty tree.
2. Start the queue with the root.
3. While the queue is non-empty: process len(queue) nodes, collecting values and
enqueuing children.
4. Append each level's list to the result.

COMPLEXITY
Time O(n), Space O(w) where w is the maximum tree width.

EDGE CASES
- Empty tree.
- Skewed tree (like a linked list).
- Single node.

FOLLOW-UPS
- Zig-zag level order.
- Right-side view of the tree.
- Maximum depth, diameter, lowest common ancestor (DFS).
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    if not root:
        return []
    levels, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):  # exactly one level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels
