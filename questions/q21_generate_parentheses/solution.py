"""Q21. Generate Parentheses  (Medium | Backtracking / Recursion)

PROBLEM
Given n pairs of parentheses, generate every well-formed combination.

CONCEPT
Backtracking builds a solution one choice at a time, explores it recursively, and UNDOES
the choice (pop) to try alternatives. The key to efficiency is pruning invalid branches
early instead of generating everything and filtering.

Two rules keep the string valid: you may add '(' while fewer than n have been used, and
you may add ')' only while closers < openers. The number of results is the n-th Catalan
number, so no algorithm can beat that.

APPROACH
1. State: current characters, count of opened, count of closed.
2. Base case: length == 2n -> save a joined string.
3. If opened < n: choose '(' , recurse, undo.
4. If closed < opened: choose ')', recurse, undo.

COMPLEXITY
Time O(4^n / sqrt(n)) (Catalan), Space O(n) recursion depth.

EDGE CASES
- n = 1 -> ['()'].
- n = 0 -> [''] (agree on behaviour).
- Use a list + join instead of string concatenation for efficiency.

FOLLOW-UPS
- Subsets, permutations and combination sum (same template).
- N-Queens: prune using column/diagonal sets.
- Word search in a grid.
"""


def generate_parentheses(n):
    result = []

    def backtrack(current, opened, closed):
        if len(current) == 2 * n:
            result.append(''.join(current))
            return
        if opened < n:
            current.append('(')
            backtrack(current, opened + 1, closed)
            current.pop()
        if closed < opened:
            current.append(')')
            backtrack(current, opened, closed + 1)
            current.pop()

    backtrack([], 0, 0)
    return result
