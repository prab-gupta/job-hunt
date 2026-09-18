"""Day 1: TS reflexes -> Python. Fill each function body. Run: python3 day1.py
All asserts must pass. Hints in comments. No peeking at CHEATSHEET.md until stuck 3 min."""

from collections import Counter, defaultdict


def double_evens(nums):
    """[1,2,3,4] -> [4,8]. Hint: one list comprehension with an `if`."""
    ...


def word_count(text):
    """'a b a' -> {'a': 2, 'b': 1}. Hint: .split() then Counter, return dict(...)."""
    ...


def top_k(counts, k):
    """{'a':3,'b':1,'c':2}, 2 -> ['a','c']. Hint: sorted(counts, key=counts.get, reverse=True)[:k]."""
    ...


def group_by(rows, key):
    """rows=[{'city':'Milan','n':1},{'city':'Rome','n':2},{'city':'Milan','n':3}], key='city'
    -> {'Milan': [row1, row3], 'Rome': [row2]}. Hint: defaultdict(list), return dict(...)."""
    ...


def safe_get(d, path, default=None):
    """d={'a':{'b':{'c':1}}}, path='a.b.c' -> 1; path='a.x.c' -> default.
    Hint: for part in path.split('.'): d = d.get(part) ... stop when not a dict."""
    ...


def dedupe_keep_order(items):
    """[3,1,3,2,1] -> [3,1,2]. Hint: a `seen` set and a result list, or dict.fromkeys."""
    ...


def flatten(nested):
    """[[1,2],[3],[]] -> [1,2,3]. Hint: nested comprehension `for sub in nested for x in sub`."""
    ...


def is_palindrome(s):
    """'Racecar' -> True, 'ab' -> False. Hint: s.lower() and s[::-1]."""
    ...


def fizzbuzz(n):
    """5 -> ['1','2','Fizz','4','Buzz']. Hint: range(1, n+1), check 15 first, str(i)."""
    ...


def merge_sorted(a, b):
    """[1,3,5],[2,4] -> [1,2,3,4,5] without sorted(). Hint: two indexes i, j and a while loop."""
    ...


if __name__ == "__main__":
    assert double_evens([1, 2, 3, 4]) == [4, 8]
    assert word_count("a b a") == {"a": 2, "b": 1}
    assert top_k({"a": 3, "b": 1, "c": 2}, 2) == ["a", "c"]
    rows = [{"city": "Milan", "n": 1}, {"city": "Rome", "n": 2}, {"city": "Milan", "n": 3}]
    assert group_by(rows, "city") == {"Milan": [rows[0], rows[2]], "Rome": [rows[1]]}
    assert safe_get({"a": {"b": {"c": 1}}}, "a.b.c") == 1
    assert safe_get({"a": {"b": {"c": 1}}}, "a.x.c", 0) == 0
    assert dedupe_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert flatten([[1, 2], [3], []]) == [1, 2, 3]
    assert is_palindrome("Racecar") and not is_palindrome("ab")
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert merge_sorted([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    print("day1: all 10 pass")
