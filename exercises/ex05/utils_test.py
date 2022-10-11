"""Importing the function from the utils file to test them."""

__author__: str = "730488308"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_empty() -> None:
    """Returning an empty list when given an empty list."""
    int_list: list[int] = []
    assert only_evens(int_list) == []


def test_only_evens_negative() -> None:
    """Returning an evens list given negative numbers."""
    int_list: list[int] = [-10, -8, -6, -4, -2, 0]
    assert only_evens(int_list) == [-10, -8, -6, -4, -2, 0]


def test_only_evens_all_evens() -> None:
    """Returning an evens list given all even numbers."""
    int_list: list[int] = [42, 44, 46, 48, 50]
    assert only_evens(int_list) == [42, 44, 46, 48, 50]


def test_concat_empty() -> None:
    """Concatenating an empty list given two empty lists."""
    firstlist: list[int] = []
    secondlist: list[int] = []
    assert concat(firstlist, secondlist) == []


def test_concat_single_index_and_empty() -> None:
    """Concatenating a list given a single index list and empty list."""
    firstlist: list[int] = [7]
    secondlist: list[int] = []
    assert concat(firstlist, secondlist) == [7]


def test_concat_different_length_lists() -> None:
    """Concatenating lists of different lengths."""
    firstlist: list[int] = [69, 1337]
    secondlist: list[int] = [420]
    assert concat(firstlist, secondlist) == [69, 1337, 420]


def test_sub_empty() -> None:
    """Forming a list based on a range of indices given an empty list."""
    mainlist: list[int] = []
    startindex: int = 0
    endindex: int = 6
    assert sub(mainlist, startindex, endindex) == []


def test_sub_both_indices_between_ends_of_list() -> None:
    """Forming a list based on starting and ending indices being within range of list."""
    mainlist: list[int] = [1, 2, 3, 4, 5, 6, 7]
    startindex: int = 2
    endindex: int = 5
    assert sub(mainlist, startindex, endindex) == [3, 4, 5]


def test_sub_negative() -> None:
    """Forming a list when the starting index is negative."""
    mainlist: list[int] = [1, 2, 3, 4]
    startindex: int = -1
    endindex: int = 2
    assert sub(mainlist, startindex, endindex) == [1, 2]
