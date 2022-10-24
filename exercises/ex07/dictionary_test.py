"""Ex07- The test file for dictionary functions."""

__author__: str = "730488308"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_edge() -> None:
    """Edge case."""
    empty_dict: dict[str, str] = {}
    assert invert(empty_dict) == {}


def test_invert_use1() -> None:
    """Use 1."""
    norm_dict: dict[str, str] = {
        "hoes": "mad",
        "comp": "110"
    }
    assert invert(norm_dict) == {"mad": "hoes", "110": "comp"}


def test_invert_use2() -> None:
    """Use 2."""
    norm_dict: dict[str, str] = {
        "poop": "book",
        "slat": "water"
    }
    assert invert(norm_dict) == {"book": "poop", "water": "slat"}


def test_favorite_color_edge() -> None:
    """Edge case."""
    empty_dict: dict[str, str] = {}
    assert favorite_color(empty_dict) == ""


def test_favorite_color_use1() -> None:
    """Use 1."""
    color_dict: dict[str, str] = {
        "tyler": "purple",
        "chi": "purple",
        "mom": "blue"
    }
    assert favorite_color(color_dict) == "purple"


def test_favorite_color_use2() -> None:
    """Use 2."""
    color_dict: dict[str, str] = {
        "leo": "red",
        "cy": "red",
        "willy": "orange",
        "bro": "orange"
    }
    assert favorite_color(color_dict) == "red"


def test_count_edge() -> None:
    """Edge case."""
    empty_list: list[str] = []
    assert count(empty_list) == {}


def test_count_use1() -> None:
    """Use 1."""
    full_list: list[str] = ["j", "j", "h", "l", "j", "l"]
    assert count(full_list) == {"j": 3, "h": 1, "l": 2}


def test_count_use2() -> None:
    """Use 2."""
    full_list: list[str] = ["e", "e", "a"]
    assert count(full_list) == {"e": 2, "a": 1}

    