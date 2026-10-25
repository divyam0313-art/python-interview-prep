# Q12. Group Anagrams

**Level:** Medium  |  **Topic:** Hashing

## Problem

Given a list of words, group the words that are anagrams of each other. The order of groups and of words inside groups does not matter.

## Signature

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
```

## Examples

```
group_anagrams(["eat","tea","tan","ate","nat","bat"])
  ->  [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

## Expected efficiency

Better than comparing every pair of words.

## Solution

See [`solution.py`](solution.py) for the concept, approach, tested code, complexity,
edge cases and follow-up questions.
