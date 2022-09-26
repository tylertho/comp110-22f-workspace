"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum([]) == 0.0


def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0


def test_sum_many_items_again() -> None:
    assert sum ([-1.0, 1.0, -2.0, 2.0]) == 0

not True or not False and True and False or not False and True and not True or False
False or True and True and False or True and True and False or False
False or False or False or False