# lcs2
`lcs2` is a Python package which helps compute the longest common subsequence of a pair of sequences.

## Installation
```
pip install lcs2
```

## Reference
The package provides the following functions:

| Function      | Signature                                           | Result                           |
|:--------------|:----------------------------------------------------|:---------------------------------|
| `lcs`         | `Iterable[T], Iterable[T] -> list[T]`               | Longest common subsequence (LCS) |
| `lcs_indices` | `Iterable[T], Iterable[T] -> list[tuple[int, int]]` | Indices of the LCS               |
| `lcs_length`  | `Iterable[T], Iterable[T] -> int`                   | Length of the LCS                |

Calling `lcs_length(a, b)` is somewhat more efficient than simply using `len(lcs(a, b))`.

## Sample Usage
```python
from lcs2 import lcs, lcs_indices, lcs_length

a = 'Hello, world!'
b = 'Foobar'
print(lcs(a, b))  # ['o', 'o', 'r']
print(lcs_indices(a, b))  # [(4, 1), (8, 2), (9, 5)]
print(lcs_length(a, b))  # 3
```
