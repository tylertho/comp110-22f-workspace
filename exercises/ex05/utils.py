"""Defining the functions to have them then be tested in the utils_tests file."""

__author__: str = "730488308"


def only_evens(int_list: list[int]) -> list[int]:
    """Taking a list and returning a new list that only contains the even numbers from the original list."""
    i: int = 0
    evens_list: list[int] = []
    while i < len(int_list):
        if int_list[i] % 2 == 0:
            evens_list.append(int_list[i])
        i += 1
    return evens_list


def concat(firstlist: list[int], secondlist: list[int]) -> list[int]:
    """Concatenating two lists of integers."""
    i: int = 0
    full_list: list[int] = firstlist
    while i < len(secondlist):
        full_list.append(secondlist[i])
        i += 1
    return full_list


def sub(mainlist: list[int], startindex: int, endindex: int) -> list[int]:
    """Forming a new list of integers between the starting and ending indices."""
    i: int = startindex
    new_list: list[int] = []
    while i < len(mainlist):
        new_list.append(mainlist[i])
        i += 1
        if i == endindex:
            return new_list
    return new_list