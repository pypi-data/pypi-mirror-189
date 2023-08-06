# lcs2
`lcs2` is a Python package which helps find the longest common subsequence of a pair of sequences and compute their diff.

## Installation
```
pip install lcs2
```

## Reference
The package provides the following functions:

| Function      | Signature                                                   | Result                                               |
|:--------------|:------------------------------------------------------------|:-----------------------------------------------------|
| `lcs`         | `Iterable[T], Iterable[T] -> list[T]`                       | Longest common subsequence (LCS)                     |
| `lcs_indices` | `Iterable[T], Iterable[T] -> list[tuple[int, int]]`         | Indices of the LCS                                   |
| `lcs_length`  | `Iterable[T], Iterable[T] -> int`                           | Length of the LCS                                    |
| `diff`        | `Iterable[T], Iterable[T] -> list[tuple[list[T], list[T]]]` | Differing segments of the sequences based on the LCS |
| `diff_ranges` | `Iterable[T], Iterable[T] -> list[tuple[range, range]]`     | Ranges of indices of the differing segments          |

Calling `lcs_length(a, b)` is somewhat more efficient than `len(lcs(a, b))`.

## Sample Usage
```python
from lcs2 import diff, diff_ranges, lcs, lcs_indices, lcs_length

a = 'Hello, world!'
b = 'Foobar'

print(lcs(a, b))  # ['o', 'o', 'r']
print(lcs_indices(a, b))  # [(4, 1), (8, 2), (9, 5)]
print(lcs_length(a, b))  # 3

print(diff(a, b))  # [(['H', 'e', 'l', 'l'], ['F']),
                   # ([',', ' ', 'w'], []),
                   # ([], ['b', 'a']),
                   # (['l', 'd', '!'], [])]
print(diff_ranges(a, b))  # [(range(0, 4), range(0, 1)),
                          # (range(5, 8), range(2, 2)),
                          # (range(9, 9), range(3, 5)),
                          # (range(10, 13), range(6, 6))]
```
