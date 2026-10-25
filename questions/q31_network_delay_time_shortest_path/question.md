# Q31. Network Delay Time (Shortest Path)

**Level:** Hard  |  **Topic:** Graphs / Dijkstra

## Problem

A network has `n` nodes (1..n). `times[i] = [u, v, w]` is a directed edge from u to v taking w time. A signal is sent from node `k`. Return the time for all nodes to receive it, or -1 if some node is unreachable.

## Signature

```python
def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
```

## Examples

```
network_delay_time([[2,1,1],[2,3,1],[3,4,1]], n=4, k=2)  ->  2
network_delay_time([[1,2,1]], n=2, k=2)  ->  -1
```

## Expected efficiency

O(E log V).

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
