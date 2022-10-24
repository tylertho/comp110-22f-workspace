"""bruh"""

a: int = 3
b: int = 0
c: float


def main() -> None:
    global a
    global b
    print(fun(a, b))


def fun(a: int, b: int) -> list[int]:
    global c
    nums: list[int] = []
    if b == 0:
        while len(nums) < 4:
            c = a + b / 2
            if c % 2 == 0:
                a += 1
                b += 1
            else: 
                nums.append(a)
                a += 3
    return nums


if __name__ == "__main__":
    main()


def odd_and_even(x: list[int]) -> list[int]:
    i: int = 0
    new_list: list[int] = []
    while i < len(x):
        if x[i] % 2 != 0:
            new_list.append(x[i])
        i += 2
    return new_list


def vowels_and_threes(y: str) -> str:
    word: str = ""
    vowels_list: list[str] = ['a', 'e', 'i', 'o', 'u']
    i: int = 0
    while i < len(y):
        if i % 3 == 0 or y[i] in vowels_list:
            if i % 3 == 0 and y[i] in vowels_list:
                word += ""
            else:
                word += y[i]
        i += 1

    return word


def vowels_and_threes_two(string: str) -> str:
    new_string: str = ""
    vowels_list: list[str] = ['a', 'e', 'i', 'o', 'u']
    i: int = 0
    while i < len(string):
        if i % 3 == 0 and string[i] in vowels_list:
            new_string += ""
        elif i % 3 == 0 or string[i] in vowels_list:
            new_string += string[i]
        i += 1

    return new_string


def average_grade(x: dict[str, list[int]]) -> dict[str, float]:
    average_dict: dict[str, float] = {}
    for name in x:
        total_grade: int = 0
        for grade in x[name]:
            total_grade += grade
            average: int = total_grade / len(x[name])
        average_dict[name] = average

    return average_dict


def reverse(string: str) -> str:
    i: int = len(string) - 1
    new: str = ""
    while i >= 0:
        new += string[i]
        i -= 1
    return new


def find_avg_score(players: dict[str, list[int]]) -> dict[str, int]:
    player_dict: dict[str, int] = {}

    for name in players:
        total: int = 0
        for score in players[name]:
            total += score
            average = total / len(players[name])
        # for finding average from a list, divide by len list
        player_dict[name] = average

    return player_dict


def join_salary_data(players: dict[int,str], salaries: dict[int, int]) -> dict[str, int]:
    name_dict: dict[str, int] = {}
    for identity in players:
        if identity in salaries:
            name_dict[players[identity]] = salaries[identity]
        else:
            name_dict[players[identity]] = -1
    return name_dict


def highest_and_lowest(items: dict[str, int]) -> dict[str, str]:
    new_dict: dict[str, str] = {
        'max': "",
        'min': ""
    }
    score_max: int = 0
    score_min: int = 0

    for name in items:
        if items[name] > score_max:
            new_dict['max'] = name
            score_max = items[name]
    
    score_min = score_max

    for name in items:
        if items[name] < score_min:
            new_dict['min'] = name
            score_min = items[name]
    
    return new_dict


def compare_scores(players: dict[str, list[int]], num_games: int) -> str:
    best_player: str = ""
    player_dict: dict[str, int] = {}
    i: int = 0
    maximum: int = 0

    while i < num_games:
        for name in players:
            if players[name][i] > maximum:
                maximum = players[name][i]
                best_player = name
            if name in player_dict:
                player_dict[name] += 1
            else:
                player_dict[name] = 1
            maximum = 0
        i += 1

    for person in player_dict:
        s_count: int = 0
        if player_dict[person] > s_count:
            s_count = player_dict[person]

    return best_player


def filter_list(characters: list[str], pairs: dict[str, int]) -> dict[str, int]:
    new_dict: dict[str, int] = {}

    for value in characters:
        new_dict[value] = 0
    
    for key in new_dict:
        if key in pairs:
            new_dict[key] = pairs[key]

    return new_dict