"""Ex07- Using dictionary functions."""

__author__: str = "730488308"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert the keys and the values."""
    inverted_dict: dict[str, str] = {}
    for key in x:
        inverted_dict[x[key]] = key
    # for new_key in inverted_dict:
    #     if inverted_dict[key] == inverted_dict[key]:
    #         raise KeyError("Can't have multiple values with same keys.")
    return inverted_dict


def favorite_color(y: dict[str, str]) -> str:
    """Given a dictionary of names and favorite colors, return the most frequent favorite color."""
    fav_color: str = ""
    color_dict: dict[str, int] = {}
    max_freq: int = 0
    for name in y:
        if y[name] in color_dict:
            color_dict[y[name]] += 1
        else:
            color_dict[y[name]] = 1

    for color in color_dict:
        color_freq: int = color_dict[color]
        if max_freq < color_freq:
            max_freq = color_freq
            fav_color = color

    return fav_color


def count(z: list[str]) -> dict[str, int]:
    """Transferring values from a list to a dictionary."""
    result: dict[str, int] = {}
    for item in z:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result
