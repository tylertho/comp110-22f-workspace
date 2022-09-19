"""Comparing different lists to see if values are equal to one another or finding the maximum of the lists."""

__author__: str = "730488308"

def all(values: list[int], number: int) -> bool:
    """Checking to see if all values in a list match a single integer."""
    i: int = 0
    match: bool = True
    while i < len(values):
        if values[i] == number:
            match = True
        else: 
            match = False
            return match
        i += 1
    return match

def max(data: list[int]) -> int:
    """Returning the maximum value from a dataset."""
    i: int = 0
    maximum: int = data[i]
    while i < len(data):
        if maximum < data[i]:
            maximum = data[i]
        i += 1
    return maximum

def is_equal(inputs_1: list[int], inputs_2: list[int]) -> bool:
    """Checking to see if all the values in one list are equal to the exact values in another list."""
    i: int = 0
    match: bool = True
    if len(inputs_1) != len(inputs_2):
        match = False
        return match
    while len(inputs_1) == len(inputs_2) and i < len(inputs_1):
        if inputs_1[i] == inputs_2[i]:
            match = True
        else:
            match = False
            return match
        i+= 1
    return match
