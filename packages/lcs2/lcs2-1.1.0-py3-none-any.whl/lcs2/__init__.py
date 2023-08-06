from typing import Iterable, TypeVar

__all__ = [
    'diff',
    'diff_ranges',
    'lcs',
    'lcs_indices',
    'lcs_length',
]

T = TypeVar('T')


def compute_matrix(a: list[T], b: list[T]) -> list[list[int]]:
    m = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for ai in range(len(a)):
        for bi in range(len(b)):
            m[ai + 1][bi + 1] = (m[ai][bi] + 1
                                 if a[ai] == b[bi]
                                 else max(m[ai][bi + 1], m[ai + 1][bi]))
    return m


def lcs_length_lists(a: list[T], b: list[T]) -> int:
    return compute_matrix(a, b)[len(a)][len(b)]


def lcs_length(a: Iterable[T], b: Iterable[T]) -> int:
    return lcs_length_lists(list(a), list(b))


def lcs_indices_lists(a: list[T], b: list[T]) -> list[tuple[int, int]]:
    m = compute_matrix(a, b)
    steps: list[tuple[int, int]] = []
    current = len(a), len(b)
    while all(current):
        ai = current[0] - 1
        bi = current[1] - 1
        if a[ai] == b[bi]:
            steps.append((ai, bi))
            current = ai, bi
        else:
            candidates = [(ai, bi + 1), (ai + 1, bi)]
            current = max(candidates, key=lambda indices: m[indices[0]][indices[1]])
    return list(reversed(steps))


def lcs_indices(a: Iterable[T], b: Iterable[T]) -> list[tuple[int, int]]:
    return lcs_indices_lists(list(a), list(b))


def lcs_lists(a: list[T], b: list[T]) -> list[T]:
    return [a[a_index] for a_index, _ in lcs_indices(a, b)]


def lcs(a: Iterable[T], b: Iterable[T]) -> list[T]:
    return lcs_lists(list(a), list(b))


def diff_ranges_lists(a: list[T], b: list[T]) -> list[tuple[range, range]]:
    ranges: list[tuple[range, range]] = []
    a_pos = 0
    b_pos = 0
    for a_index, b_index in lcs_indices_lists(a, b) + [(len(a), len(b))]:
        if a_index > a_pos or b_index > b_pos:
            ranges.append((range(a_pos, a_index), range(b_pos, b_index)))
        a_pos = a_index + 1
        b_pos = b_index + 1
    return ranges


def diff_ranges(a: Iterable[T], b: Iterable[T]) -> list[tuple[range, range]]:
    return diff_ranges_lists(list(a), list(b))


def diff_lists(a: list[T], b: list[T]) -> list[tuple[list[T], list[T]]]:
    return [([a[i] for i in a_range], [b[i] for i in b_range])
            for a_range, b_range in diff_ranges_lists(a, b)]


def diff(a: Iterable[T], b: Iterable[T]) -> list[tuple[list[T], list[T]]]:
    return diff_lists(list(a), list(b))
