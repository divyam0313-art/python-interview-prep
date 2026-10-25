"""Q27. Course Schedule (Ordering with Prerequisites)  (Hard | Graphs / Topological Sort)

PROBLEM
There are num_courses courses labelled 0..n-1. Each pair [a, b] in prerequisites means
you must take b before a. Return a valid order to finish all courses, or an empty list
if it is impossible (a cycle exists).

CONCEPT
A TOPOLOGICAL ORDER of a directed acyclic graph (DAG) lists every node after all of its
prerequisites. It exists if and only if the graph has no cycle. Real uses: build
systems, task schedulers, dependency resolution (pip, Airflow DAGs).

Kahn's algorithm: compute each node's in-degree (number of unmet prerequisites), start
with all in-degree-0 nodes in a queue, and repeatedly remove one, 'completing' it by
decrementing its neighbours. If we process fewer than n nodes, the rest are stuck in a
cycle. The DFS alternative uses three colours (unvisited / visiting / done) to detect
back edges.

APPROACH
1. Build adjacency list pre -> [courses] and in-degree array.
2. Queue all nodes with in-degree 0.
3. Pop, append to order, decrement neighbours; enqueue those that reach 0.
4. If len(order) == num_courses return it, else [].

COMPLEXITY
Time O(V + E), Space O(V + E).

EDGE CASES
- No prerequisites -> any order.
- Self-loop [0,0] is a cycle.
- Disconnected components.

FOLLOW-UPS
- Only report whether finishing is possible (Course Schedule I).
- Return the cycle itself.
- Parallel semesters: minimum number of rounds (level-by-level Kahn).
"""
from collections import defaultdict
from collections import deque


def find_order(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1
    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == num_courses else []  # [] means a cycle
