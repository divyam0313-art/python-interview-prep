import asyncio
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from loader import *


def build_list(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 3], 6) == [0, 1] and two_sum([1, 2], 9) == []

assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False and is_palindrome("") is True

assert is_valid_parentheses("()[]{}") and not is_valid_parentheses("(]")
assert not is_valid_parentheses("((") and not is_valid_parentheses("]")

a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(a)
assert k == 5 and a[:k] == [0, 1, 2, 3, 4] and remove_duplicates([]) == 0

assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([-3, -1, -2]) == -1

assert first_occurrence([1, 2, 2, 2, 3], 2) == 1
assert first_occurrence([1, 3], 2) == -1 and first_occurrence([], 1) == -1

assert to_list(reverse_list(build_list([1, 2, 3, 4]))) == [4, 3, 2, 1]
assert reverse_list(None) is None

assert list(flatten([1, [2, [3, [4]], 5], (6, 7), "ab"])) == [1, 2, 3, 4, 5, 6, 7, "ab"]

assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49 and max_area([1, 1]) == 1

assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]] and three_sum([1, 2]) == []

assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("abba") == 2 and length_of_longest_substring("") == 0

g = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
assert sorted(sorted(x) for x in g) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([1, 0, 3, 4]) == [0, 12, 0, 0]

assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]] and merge_intervals([]) == []

t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert level_order(t) == [[3], [9, 20], [15, 7]] and level_order(None) == []

grid = ["11000", "11000", "00100", "00011"]
assert num_islands(grid) == 3 and num_islands([]) == 0

assert rob([2, 7, 9, 3, 1]) == 12 and rob([]) == 0 and rob([5]) == 5

assert coin_change([1, 2, 5], 11) == 3 and coin_change([2], 3) == -1
assert coin_change([1], 0) == 0

assert subarray_sum([1, 1, 1], 2) == 2 and subarray_sum([1, -1, 0], 0) == 3

assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

assert sorted(generate_parentheses(3)) == sorted(
    ["((()))", "(()())", "(())()", "()(())", "()()()"])
assert generate_parentheses(1) == ["()"]

for cls in (LRUCache, LRUCacheManual):
    c = cls(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1 and c.get(3) == 3 and c.get(4) == 4
    c.put(3, 30)
    assert c.get(3) == 30

clock = [0.0]
calls = []


@ttl_cache(10, timer=lambda: clock[0])
def slow(x, y=1):
    calls.append((x, y))
    return x * y


assert slow(2, y=3) == 6 and slow(2, y=3) == 6 and len(calls) == 1
clock[0] = 11
assert slow(2, y=3) == 6 and len(calls) == 2
assert slow.__name__ == "slow"

assert lcs_length("abcde", "ace") == 3 and lcs_length("abc", "def") == 0
assert lcs_length("", "abc") == 0

assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9 and trap([]) == 0 and trap([3]) == 0

assert min_window("ADOBECODEBANC", "ABC") == "BANC"
assert min_window("a", "a") == "a" and min_window("a", "aa") == ""
assert min_window("aa", "aa") == "aa"

order = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
assert order[0] == 0 and order[-1] == 3 and len(order) == 4
assert find_order(2, [[1, 0], [0, 1]]) == [] and find_order(1, []) == [0]

assert edit_distance("horse", "ros") == 3
assert edit_distance("intention", "execution") == 5 and edit_distance("", "abc") == 3

assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert length_of_lis([]) == 0 and length_of_lis([7, 7, 7]) == 1

assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6], []]) == [1, 1, 2, 3, 4, 4, 5, 6]
assert merge_k_sorted([]) == []

assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
assert network_delay_time([[1, 2, 1]], 2, 2) == -1


async def main():
    running = peak = 0

    def make(i):
        async def job():
            nonlocal running, peak
            running += 1
            peak = max(peak, running)
            await asyncio.sleep(0.01)
            running -= 1
            if i == 3:
                raise ValueError("boom")
            return i * 10
        return job

    res = await run_bounded([make(i) for i in range(8)], limit=3)
    assert peak == 3, peak
    assert res[0] == 0 and res[7] == 70 and isinstance(res[3], ValueError)


asyncio.run(main())
print("ALL TESTS PASSED")
