"""Q31. Network Delay Time (Shortest Path)  (Hard | Graphs / Dijkstra)

PROBLEM
A network has n nodes (1..n). times[i] = [u, v, w] is a directed edge from u to v taking
w time. A signal is sent from node k. Return the time for all nodes to receive it, or -1
if some node is unreachable.

CONCEPT
With non-negative edge weights, DIJKSTRA's algorithm finds shortest distances from a
source. Greedy idea: the unvisited node with the smallest tentative distance is already
final, because any other route to it would pass through a node at least as far away.

Use a min-heap of (distance, node). Python's heapq has no decrease-key, so we push
duplicates and skip stale entries when popped (if u in dist: continue). The answer is
the MAXIMUM shortest distance (the last node to hear the signal). Use BFS for unweighted
graphs, Dijkstra for non-negative weights, Bellman-Ford if negative weights exist.

APPROACH
1. Build adjacency list u -> [(v, w)].
2. Heap starts with (0, k).
3. Pop (d, u); skip if already finalised; record dist[u] = d.
4. Push (d + w, v) for unfinalised neighbours.
5. If fewer than n nodes finalised -> -1, else max(dist.values()).

COMPLEXITY
Time O(E log V), Space O(V + E).

EDGE CASES
- Unreachable nodes -> -1.
- n = 1 and no edges -> 0.
- Parallel edges with different weights.

FOLLOW-UPS
- Print the actual path (store parents).
- Negative weights -> Bellman-Ford.
- A* search and cheapest flights within K stops.
"""
import heapq
from collections import defaultdict


def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {}
    heap = [(0, k)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in dist:
            continue  # stale entry, a shorter path was already finalised
        dist[u] = d
        for v, w in graph[u]:
            if v not in dist:
                heapq.heappush(heap, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1
