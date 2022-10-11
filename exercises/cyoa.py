"""Making a poor rendition of Pokemon."""


__author__: str = "730488308"

from random import randint


points: int = 0
player: str = ""
current: str = ""
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


def main() -> None:
    """The main function that runs the game."""
    global all_user_pokemon_status
    global c_user_pokemon_status
    global t_user_pokemon_status
    global m_user_pokemon_status
    global current

    greet()

    print("For your starter pokemon, you may choose Charizard, Tyranitar, or Metagross.")
    starter: int = int(input("Type 1 for Charizard," + FIRE_TYPE + DRAGON_TYPE + ", 2 for Tyranitar," + ROCK_TYPE + DARK_TYPE + ", or 3 for Metagross," + PSYCHIC_TYPE + STEEL_TYPE + ":"))

    if starter == 1:
        current = "Charizard" + FIRE_TYPE + DRAGON_TYPE
    elif starter == 2:
        current = "Tyranitar" + ROCK_TYPE + DARK_TYPE
    elif starter == 3:
        current = "Metagross" + PSYCHIC_TYPE + STEEL_TYPE
    print(f"\nGreat, you have selected {current} as your starter pokemon!")

    battle_choice: int = encounter()

    while all_user_pokemon_status is True:
        if battle_choice == 1:
            current_user_pokemon: bool = path1()
        if battle_choice == 2 or current_user_pokemon is False:
            path2()
        if battle_choice == 3:
            path3()
        
        if c_user_pokemon_status is False and t_user_pokemon_status is False and m_user_pokemon_status is False:
            all_user_pokemon_status = False

        if all_user_pokemon_status is False:
            path3()

        if current_user_pokemon is False and all_user_pokemon_status is True:
            battle_choice = new_turn()
        

def greet() -> None:
    """Having the user start the game."""
    global player
    global current
    player = input("Hello, new Pokemon Trainer! What would you like to go by? ")
    print(f"\nWelcome, {player}! To begin your journey, you must choose a pokemon to start with.")

    
def encounter() -> int:
    """Having the user make a choice between 3 options."""
    print("\nYou have encountered another trainer who challenges you to a battle!")
    print("You can either attack, switch pokemon, or flee the battle.")
    choice: int = int(input("Type 1 to attack, 2 to switch pokemon, or 3 to flee: "))
    return choice


def new_turn() -> int:
    """Prompts three choices for user after user pokemon dies."""
    new_choice: int = int(input("You may choose a new battle choice: "))
    return new_choice


def path1() -> bool:
    """The first option: attack."""
    global current
    global points
    global c_user_pokemon_status
    global t_user_pokemon_status
    global m_user_pokemon_status
    global all_user_pokemon_status
    user_move: dict[int, str]
    user_move = dict()
    opp_move: dict[int, str]
    opp_move = dict()
    opp_pokemon: dict[int, str]
    opp_pokemon = dict()
    user_choice: int = 0
    opp_random: int = randint(1, 3)
    rand_move: int = randint(1, 2)
    opp_damage: int = 0
    user_damage: int = 0
    new_opp_health: int = 0
    old_opp_health: int = 0
    new_user_health: int = 0
    old_user_health: int = 0
    opp_pokemon_status: bool = True
    user_attack_status: bool = False

    opp_pokemon = {
        1: "Arcanine",
        2: "Scizor",
        3: "Honchkrow"
    }

    print("You have chosen to attack.")

    if 1 in opp_pokemon and opp_random == 1:
        opp_move = {
            1: "Fire Fang",
            2: "Crunch"
        }
        opp_damage = arcanine(rand_move)
        old_opp_health = a_health
        new_opp_health = old_opp_health
    if 2 in opp_pokemon and opp_random == 2:
        opp_move = {
            1: "Air Slash",
            2: "Steel Wing"
        }
        opp_damage = scizor(rand_move)
        old_opp_health = s_health
        new_opp_health = old_opp_health
    if 3 in opp_pokemon and opp_random == 3:
        opp_move = {
            1: "Dark Pulse",
            2: "Peck"
        }
        opp_damage = honchkrow(rand_move)
        old_opp_health = h_health
        new_opp_health = old_opp_health

    while all_user_pokemon_status is True:
        if opp_pokemon_status is False:
            opp_random = randint(1, 3)
            rand_move = randint(1, 2)
            if 1 in opp_pokemon and opp_random == 1:
                opp_move = {
                    1: "Fire Fang",
                    2: "Crunch"
                }
                opp_damage = arcanine(rand_move)
                old_opp_health = a_health
                new_opp_health = old_opp_health
            elif 2 in opp_pokemon and opp_random == 2:
                opp_move = {
                    1: "Air Slash",
                    2: "Steel Wing"
                }
                opp_damage = scizor(rand_move)
                old_opp_health = s_health
                new_opp_health = old_opp_health
            elif 3 in opp_pokemon and opp_random == 3:
                opp_move = {
                    1: "Dark Pulse",
                    2: "Peck"
                }
                opp_damage = honchkrow(rand_move)
                old_opp_health = h_health
                new_opp_health = old_opp_health
            opp_pokemon_status = True

        if current == "Charizard" + FIRE_TYPE + DRAGON_TYPE:
            if c_user_pokemon_status is True:
                old_user_health = c_health
                if user_attack_status is False:
                    new_user_health = old_user_health
                user_move = {
                    1: "Flamethrower",
                    2: "Fire Blast",
                    3: "Steel Wing",
                    4: "Dragon Claw"
                }
                print("\nYou may choose between four moves to attack: ")
                print("Flamethrower, Fire Blast, Steel Wing, or Dragon Claw.")
                user_choice = int(input("Type 1 for Flamethrower, 2 for Fire Blast, 3 for Steel Wing, or 4 for Dragon Claw: "))
                while user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4:
                    user_choice = int(input("Sorry, that input was not between 1 and 4. Try again: "))
                user_damage = charizard(user_choice)
                print(f"\nYou have chosen {user_move[user_choice]}!")
                new_opp_health -= user_damage
                if new_opp_health < 0:
                    new_opp_health = 0
                    opp_pokemon_status = False
                    points += 1
                print(f"You have dealt {str(user_damage)} damage to the opposing {opp_pokemon[opp_random]}!")
                print(f"{opp_pokemon[opp_random]} HP: {new_opp_health} / {old_opp_health}")
                if opp_pokemon_status is True:
                    new_user_health -= opp_damage
                    user_attack_status = True
                    print(f"\n{opp_pokemon[opp_random]} used {opp_move[rand_move]} and dealt {opp_damage} damage!")
                    if new_user_health <= 0:
                        new_user_health = 0
                        c_user_pokemon_status = False
                    print(f"{current} HP: {new_user_health} / {old_user_health}")
                    if c_user_pokemon_status is False:
                        print(f"Oh no, {current} has fainted!")
                        return c_user_pokemon_status
                else:
                    print(f"{opp_pokemon[opp_random]} has fainted! The opponent will now choose another pokemon to use in battle!")
                    print(f"You have defeated {points} pokemon so far!")

        if current == "Tyranitar" + ROCK_TYPE + DARK_TYPE:
            if t_user_pokemon_status is True:
                old_user_health = t_health
                if user_attack_status is False:
                    new_user_health = old_user_health
                user_move = {
                    1: "Earthquake",
                    2: "Ice Fang",
                    3: "Rock Slide",
                    4: "Dark Pulse"
                }
                print("\nYou may choose between four moves to attack: ")
                print("Earthquake, Ice Fang, Rock Slide, or Dark Pulse.")
                user_choice = int(input("Type 1 for Earthquake, 2 for Ice Fang, 3 for Rock Slide, or 4 for Dark Pulse: "))
                while user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4:
                    user_choice = int(input("Sorry, that input was not between 1 and 4. Try again: "))
                user_damage = tyranitar(user_choice)
                print(f"\nYou have chosen {user_move[user_choice]}!")
                new_opp_health -= user_damage
                if new_opp_health < 0:
                    new_opp_health = 0
                    opp_pokemon_status = False
                    points += 1
                print(f"You have dealt {str(user_damage)} damage to the opposing {opp_pokemon[opp_random]}!")
                print(f"{opp_pokemon[opp_random]} HP: {new_opp_health} / {old_opp_health}")
                if opp_pokemon_status is True:
                    new_user_health -= opp_damage
                    user_attack_status = True
                    print(f"\n{opp_pokemon[opp_random]} used {opp_move[rand_move]} and dealt {opp_damage} damage!")
                    if new_user_health <= 0:
                        new_user_health = 0
                        t_user_pokemon_status = False
                    print(f"{current} HP: {new_user_health} / {old_user_health}")
                    if t_user_pokemon_status is False:
                        print(f"Oh no, {current} has fainted!")
                        return t_user_pokemon_status
                else:
                    print(f"{opp_pokemon[opp_random]} has fainted! The opponent will now choose another pokemon to use in battle!")
                    print(f"You have defeated {points} pokemon so far!")

        if current == "Metagross" + PSYCHIC_TYPE + STEEL_TYPE:
            if m_user_pokemon_status is True:
                old_user_health = m_health
                if user_attack_status is False:
                    new_user_health = old_user_health
                user_move = {
                    1: "Psychic",
                    2: "Shadow Ball",
                    3: "Flash Cannon",
                    4: "Brick Break"
                }
                print("\nYou may choose between four moves to attack: ")
                print("Psychic, Shadow Ball, Flash Cannon, or Brick Break.")
                user_choice = int(input("Type 1 for Psychic, 2 for Shadow Ball, 3 for Flash Cannon, or 4 for Brick Break: "))
                while user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4:
                    user_choice = int(input("Sorry, that input was not between 1 and 4. Try again: "))
                user_damage = metagross(user_choice)
                print(f"\nYou have chosen {user_move[user_choice]}!")
                new_opp_health -= user_damage
                if new_opp_health < 0:
                    new_opp_health = 0
                    opp_pokemon_status = False
                    points += 1
                print(f"You have dealt {str(user_damage)} damage to the opposing {opp_pokemon[opp_random]}!")
                print(f"{opp_pokemon[opp_random]} HP: {new_opp_health} / {old_opp_health}")
                if opp_pokemon_status is True:
                    new_user_health -= opp_damage
                    user_attack_status = True
                    print(f"\n{opp_pokemon[opp_random]} used {opp_move[rand_move]} and dealt {opp_damage} damage!")
                    if new_user_health <= 0:
                        new_user_health = 0
                        m_user_pokemon_status = False
                    print(f"{current} HP: {new_user_health} / {old_user_health}")
                    if m_user_pokemon_status is False:
                        print(f"Oh no, {current} has fainted!")
                        return m_user_pokemon_status
                else:
                    print(f"{opp_pokemon[opp_random]} has fainted! The opponent will now choose another pokemon to use in battle!")
                    print(f"You have defeated {points} pokemon so far!")
    
        if c_user_pokemon_status is False and t_user_pokemon_status is False and m_user_pokemon_status is False:
            all_user_pokemon_status = False
    
    if all_user_pokemon_status is False:
        return False


def path2() -> None:
    """The second option: switch pokemon."""
    global current
    if current == "Charizard" + FIRE_TYPE + DRAGON_TYPE:
        path2_charizard()
        return None
    if current == "Tyranitar" + ROCK_TYPE + DARK_TYPE:
        path2_tyranitar()
        return None
    if current == "Metagross" + PSYCHIC_TYPE + STEEL_TYPE:
        path2_metagross()
        return None


def path2_charizard() -> None:
    """Switching from Charizard if current."""
    global current
    if t_user_pokemon_status is True and m_user_pokemon_status is True:
        current_int = int(input("Type 2 to switch to Tyranitar or 3 to switch to Metagross: "))
        if current_int == 2:
            current = "Tyranitar" + ROCK_TYPE + DARK_TYPE
            return None
        if current_int == 3:
            current = "Metagross" + PSYCHIC_TYPE + STEEL_TYPE
            return None
    else:
        if t_user_pokemon_status is True:
            current_int = int(input("Type 2 to switch to Tyranitar: "))
            if current_int == 2:
                current = "Tyranitar" + ROCK_TYPE + DARK_TYPE
                return None
        if m_user_pokemon_status is True:
            current_int = int(input("Type 3 to switch to Metagross: "))
            if current_int == 3:
                current = "Metagross" + PSYCHIC_TYPE + STEEL_TYPE
                return None


def path2_tyranitar() -> None:
    """Switching from Tyranitar if current."""
    global current
    if c_user_pokemon_status is True and m_user_pokemon_status is True:
        current_int = int(input("Type 1 to switch to Charizard or 3 to switch to Metagross: "))
        if current_int == 1:
            current = "Charizard" + FIRE_TYPE + DRAGON_TYPE
            return None
        if current_int == 3:
            current = "Metagross" + PSYCHIC_TYPE + STEEL_TYPE
            return None
    else:
        if c_user_pokemon_status is True:
            current_int = int(input("Type 1 to switch to Charizard: "))
            if current_int == 1:
                current = "Charizard" + FIRE_TYPE + DRAGON_TYPE
                return None
        if m_user_pokemon_status is True:
            current_int = int(input("Type 3 to switch to Metagross: "))
            if current_int == 3:
                current = "Metagross" + PSYCHIC_TYPE + STEEL_TYPE
                return None


def path2_metagross() -> None:
    """Switching from Metagross if current."""
    global current
    if c_user_pokemon_status is True and t_user_pokemon_status is True:
        current_int: int = int(input("Type 1 to switch to Charizard or 2 to switch to Tyranitar: "))
        if current_int == 1:
            current = "Charizard" + FIRE_TYPE + DRAGON_TYPE
            return None
        elif current_int == 2:
            current = "Tyranitar" + ROCK_TYPE + DARK_TYPE
            return None
    else:
        if c_user_pokemon_status is True:
            current_int = int(input("Type 1 to switch to Charizard: "))
            if current_int == 1:
                current = "Charizard" + FIRE_TYPE + DRAGON_TYPE
                return None
        elif t_user_pokemon_status is True:
            current_int = int(input("Type 2 to switch to Tyranitar: "))
            if current_int == 2:
                current = "Tyranitar" + ROCK_TYPE + DARK_TYPE
                return None


def path3() -> None:
    """The third option: flee or end the game."""
    print(f"\nYou defeated {points} pokemon!")
    print(f"Thanks for playing, {player}!")
    quit()


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
    else:
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
    else:
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
    else:
        return brick_break[0]


# opposing trainer pokemon
def arcanine(x: int) -> int:
    """Moves of opposing pokemon: Arcanine."""
    fire_fang: dam_type = (65, "Fire", FIRE_TYPE, 1)
    crunch: dam_type = (60, "Dark", DARK_TYPE, 2)
    print("\nYour opponent has chosen Arcanine" + FIRE_TYPE + DOG + "!")

    if x == fire_fang[3]:
        return fire_fang[0]
    else:
        return crunch[0]


def scizor(x: int) -> int:
    """Moves of opposing pokemon: Scizor."""
    air_slash: dam_type = (50, "Flying", FLYING_TYPE, 1)
    steel_wing: dam_type = (70, "Steel", STEEL_TYPE, 2)
    print("\nYour opponent has chosen Scizor" + BUG_TYPE + FLYING_TYPE + "!")

    if x == air_slash[3]:
        return air_slash[0]
    else:
        return steel_wing[0]


def honchkrow(x: int) -> int:
    """Moves of opposing pokemon: Honchkrow."""
    dark_pulse: dam_type = (80, "Dark", DARK_TYPE, 1)
    peck: dam_type = (35, "Flying", DARK_TYPE, 2)
    print("\nYour opponent has chosen Honchkrow" + DARK_TYPE + FLYING_TYPE + "!")

    if x == dark_pulse[3]:
        return dark_pulse[0]
    else:
        return peck[0]


if __name__ == "__main__":
    main()