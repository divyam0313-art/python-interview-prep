"""Q22. Design an LRU Cache  (Medium | Design / Data Structures)

PROBLEM
Design a Least Recently Used cache with get(key) and put(key, value) both in O(1). When
capacity is exceeded, evict the least recently used entry. get of a missing key returns
-1. First solve it with the standard library, then implement it from scratch.

CONCEPT
O(1) lookup needs a hash map; O(1) 'move to most-recent' and 'evict oldest' needs an
ordering structure with O(1) removal anywhere - a DOUBLY linked list. The classic LRU is
the combination: dict maps key -> list node.

Python gives you a shortcut: collections.OrderedDict is a dict that remembers order,
with move_to_end and popitem(last=False) both O(1). Since Python 3.7 a normal dict
preserves insertion order too, but OrderedDict's move_to_end is what makes LRU trivial.
Interviewers often then say 'now without OrderedDict', so know the sentinel-node linked-
list version.

APPROACH
1. Version 1: OrderedDict. get -> move_to_end and return. put -> insert/update,
move_to_end, pop oldest if over capacity.
2. Version 2: dict + doubly linked list with HEAD and TAIL sentinel nodes (avoids None
checks).
3. Most recent lives right after head; least recent is tail.prev.
4. Every access = unlink the node and re-insert after head.

COMPLEXITY
Time O(1) per operation, Space O(capacity).

EDGE CASES
- Updating an existing key must refresh its recency and not grow the size.
- Capacity 1.
- Evicting must delete from BOTH the list and the dict.

FOLLOW-UPS
- Make it thread-safe (a lock, or per-shard locks).
- Add TTL expiry (Q23).
- LFU cache (least frequently used) in O(1).
- functools.lru_cache - how does it work and what are its pitfalls (unhashable args,
memory growth)?
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)  # mark as most recently used
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)  # evict least recently used


class _Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCacheManual:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head, self.tail = _Node(), _Node()  # sentinels
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _add_front(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._add_front(node)
        return node.value

    def put(self, key, value):
        node = self.map.get(key)
        if node:
            node.value = value
            self._remove(node)
        else:
            node = self.map[key] = _Node(key, value)
            if len(self.map) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
        self._add_front(node)
