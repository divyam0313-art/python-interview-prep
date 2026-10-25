"""Q16. Number of Islands  (Medium | Graphs / Grid DFS)

PROBLEM
Given a 2-D grid of '1' (land) and '0' (water), count the islands. An island is a group
of land cells connected horizontally or vertically.

CONCEPT
A grid is an implicit graph: each cell is a node with up to 4 neighbours. Counting
'connected components' is done by scanning every cell; whenever we meet unvisited land
we increment the counter and FLOOD-FILL the entire island so it is never counted again.

Flood fill can be recursive DFS, iterative DFS (stack) or BFS (queue). Recursive DFS may
hit Python's recursion limit on a 1000x1000 grid, so an explicit stack is the
production-safe choice. Marking visited cells in place avoids a separate visited set,
but copy the grid first if the caller's data must stay intact.

APPROACH
1. Copy the grid into lists of characters.
2. Scan each cell; on '1' increment count.
3. Push the cell on a stack and mark it '0'.
4. Pop cells, pushing every in-bounds land neighbour (marking it '0' immediately).

COMPLEXITY
Time O(R x C), Space O(R x C) worst case for the stack.

EDGE CASES
- Empty grid.
- All water / all land.
- Diagonals do NOT connect (clarify).

FOLLOW-UPS
- Maximum area of an island.
- Union-Find solution for a dynamic stream of land additions.
- Surrounded regions / rotting oranges (multi-source BFS).
"""


def num_islands(grid):
    grid = [list(row) for row in grid]  # do not mutate caller's data
    rows, cols = len(grid), len(grid[0]) if grid else 0
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '1':
                continue
            count += 1
            stack = [(r, c)]
            grid[r][c] = '0'
            while stack:
                x, y = stack.pop()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        stack.append((nx, ny))
    return count
