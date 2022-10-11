"""Making a poor rendition of Pokemon."""


__author__: str = "730488308"

from random import randint


points: int = 0
player: str = ""
current: str = ""
current2: dict[int, str]
# I was looking to do more with this tuple but I don't have time :/. I could've used just a list or dictionary
dam_type = tuple[int, str, str, int]

c_user_pokemon_status: bool = True
t_user_pokemon_status: bool = True
m_user_pokemon_status: bool = True
all_user_pokemon_status: bool = True


# These values are made by me
c_health: int = 266
t_health: int = 310
m_health: int = 270
a_health: int = 132
s_health: int = 107
h_health: int = 123

FIRE_TYPE: str = "\U0001F525"
FLYING_TYPE: str = "\U00002601"
DARK_TYPE: str = "\U00002B1B"
ROCK_TYPE: str = "\U0001F7EB"
STEEL_TYPE: str = "\U00002B1C"
PSYCHIC_TYPE: str = "\U0001F7EA"
DRAGON_TYPE: str = "\U0001F432"
ICE_TYPE: str = "\U0001F9CA"
GHOST_TYPE: str = "\U0001F47B"
FIGHTING_TYPE: str = "\U0001F44A"
GROUND_TYPE: str = "\U0001F30D"
BUG_TYPE: str = "\U0001F41D"
DOG: str = "\U0001F436"


def greet() -> None:
    """Having the user start the game."""
    global player
    global current
    player = input("Hello, new Pokemon Trainer! What would you like to go by: ")
    print(f"\nWelcome, {player}! To begin your journey, you must choose a pokemon to start with.")
    print("For your starter pokemon, you may choose Charizard, Tyranitar, or Metagross.")
    starter: int = int(input("Type 1 for Charizard," + FIRE_TYPE + DRAGON_TYPE + ", 2 for Tyranitar," + ROCK_TYPE + DARK_TYPE + ", or 3 for Metagross," + PSYCHIC_TYPE + STEEL_TYPE + ":"))

    if starter == 1:
        current = "charizard" # "Charizard" + FIRE_TYPE + DRAGON_TYPE
    elif starter == 2:
        current = "tyranitar"# "Tyranitar" + ROCK_TYPE + DARK_TYPE
    elif starter == 3:
        current = "metagross" # "Metagross" + PSYCHIC_TYPE + STEEL_TYPE
    print(f"\nGreat, you have selected {current} as your starter pokemon!")

def encounter() -> int:
    """Having the user make a choice between 3 options."""
    print("\nYou have encountered another trainer who challenges you to a battle!")
    print("You can either attack, switch pokemon, or flee the battle.")
    choice: int = int(input("Type 1 to attack, 2 to switch pokemon, or 3 to flee: "))
    return choice


# Given an integer, choose a move and return the damage
def charizard(x: int) -> int:
    """Moves of starter: Charizard."""
    flamethrower: dam_type = (90, "Fire", FIRE_TYPE, 1)
    fire_blast: dam_type = (110, "Fire", FIRE_TYPE, 2)
    steel_wing: dam_type = (70, "Steel", STEEL_TYPE, 3)
    dragon_claw: dam_type = (80, "Dragon", DRAGON_TYPE, 4)

    if x == flamethrower[3]:
        return flamethrower[0]
    elif x == fire_blast[3]:
        return fire_blast[0]
    elif x == steel_wing[3]:
        return steel_wing[0]
    elif x == dragon_claw[3]:
        return dragon_claw[0]


def tyranitar(x: int) -> int:
    """Moves of starter: Tyranitar."""
    earthquake: dam_type = (100, "Ground", GROUND_TYPE, 1)
    ice_fang: dam_type = (65, "Ice", ICE_TYPE, 2)
    rock_slide: dam_type = (75, "Rock", ROCK_TYPE, 3)
    dark_pulse: dam_type = (80, "Dark", DARK_TYPE, 4)

    if x == earthquake[3]:
        return earthquake[0]
    elif x == ice_fang[3]:
        return ice_fang[0]
    elif x == rock_slide[3]:
        return rock_slide[0]
    elif x == dark_pulse[3]:
        return dark_pulse[0]


def metagross(x: int) -> int:
    """Moves of starter: Metagross."""
    psychic: dam_type = (90, "Psychic", PSYCHIC_TYPE, 1)
    shadow_ball: dam_type = (80, "Ghost", GHOST_TYPE, 2)
    flash_cannon: dam_type = (80, "Steel", STEEL_TYPE, 3)
    brick_break: dam_type = (75, "Fighting", FIGHTING_TYPE, 4)

    if x == psychic[3]:
        return psychic[0]
    elif x == shadow_ball[3]:
        return shadow_ball[0]
    elif x == flash_cannon[3]:
        return flash_cannon[0]
    elif x == brick_break[3]:
        return brick_break[0]


# opposing trainer pokemon
def arcanine(x: int) -> int:
    """Moves of opposing pokemon: Arcanine."""
    fire_fang: dam_type = (65, "Fire", FIRE_TYPE, 1)
    crunch: dam_type = (60, "Dark", DARK_TYPE, 2)
    print("\nYour opponent has chosen Arcanine" + FIRE_TYPE + DOG + "!")

    if x == fire_fang[3]:
        return fire_fang[0]
    elif x == crunch[3]:
        return crunch[0]


def scizor(x: int) -> int:
    """Moves of opposing pokemon: Scizor."""
    air_slash: dam_type = (50, "Flying", FLYING_TYPE, 1)
    steel_wing: dam_type = (70, "Steel", STEEL_TYPE, 2)
    print("\nYour opponent has chosen Scizor" + BUG_TYPE + FLYING_TYPE + "!")

    if x == air_slash[3]:
        return air_slash[0]
    elif x == steel_wing[3]:
        return steel_wing[0]


def honchkrow(x: int) -> int:
    """Moves of opposing pokemon: Honchkrow."""
    dark_pulse: dam_type = (80, "Dark", DARK_TYPE, 1)
    peck: dam_type = (35, "Flying", DARK_TYPE, 2)
    print("\nYour opponent has chosen Honchkrow" + DARK_TYPE + FLYING_TYPE + "!")

    if x == dark_pulse[3]:
        return dark_pulse[0]
    elif x == peck[3]:
        return peck[0]


# if __name__ == "__main__":
#     main()