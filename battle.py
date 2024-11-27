import itertools
from healing import *
import random
from characters import make_final_boss
from movement import text_delay


def move_choice(monster: dict) -> str:
    """
    Select monster move.

    This function accesses the monster move dictionary and prompts the user to select one of 2 the moves,
    preventing any other input.

    :param monster: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: get user input and access monster moves, if move exists otherwise get user input
    :return: monster move
    :raises: IndexError if user inputs out of range

    >>> test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,'moves': {'ember': {'power': 5, 'accuracy': 80},\
    'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2} # doctest: +SKIP
    >>> move_choice(monster) # doctest: +SKIP
    'ember'
    >>> move_choice(monster) # doctest: +SKIP
    'scratch'
    """
    while True:
        move_names = list(monster['moves'].keys())
        text_delay(
            f"1. {move_names[0].capitalize()} (Power: {monster['moves'][move_names[0]]['power']},"
            f" Accuracy: {monster['moves'][move_names[0]]['accuracy']}%)\n")
        text_delay(
            f"2. {move_names[1].capitalize()} (Power: {monster['moves'][move_names[1]]['power']},"
            f" Accuracy: {monster['moves'][move_names[1]]['accuracy']}%)\n")
        move_input = input("Choose a move (1 or 2):\n")

        try:
            choice = int(move_input) - 1
            return move_names[choice]
        except (ValueError, IndexError):
            text_delay("Invalid choice! \n Please enter '1' or '2'")


def battle(monster: dict, enemy: dict) -> str:
    """
    Simulate battle

    This function takes the monster and enemy dictionaries and allows user input to effect hp using moves and their
    power

    :param monster: a dictionary
    :param enemy: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :precondition: enemy is a well-formed dictionary that represents an enemy
    :postcondition: take user input to select move names, apply the power value to reduce your hp of opponent
    :return: "Monster Wins!" or "Enemy Wins!"

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80},\
    'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    >>> battle(test_monster, test_enemy) # doctest: +SKIP
    "Monster wins!"
    >>> battle(test_monster, test_enemy) # doctest: +SKIP
    "Enemy wins!"
    """
    enemy_move_cycle = itertools.cycle(enemy['moves'])
    text_delay("The battle begins!\n")
    while is_alive(monster):
        text_delay(f"{monster['name']} turn:\n")
        move = move_choice(monster)
        use_move(monster, enemy, move)
        if enemy['hp'] <= 0:
            text_delay(f"{enemy['name']} defeated!\n")
            monster['wins'] += 1
            enemy['hp'] = enemy['max_hp']
            use_potion(monster)
            return f"{monster['name']} wins!\n"
        text_delay(f"{enemy['name']} turn:\n")
        enemy_move = next(enemy_move_cycle)
        use_move(enemy, monster, enemy_move)
        if monster['hp'] <= 0:
            text_delay("Monster defeated! Sent back to start.\n")
            return "Enemy wins!"

    text_delay("Battle over!")


def use_move(monster: dict, enemy: dict, move_name: str):
    """
    Use move

    This function gets the monster and enemies moves, check if they pass the accuracy check then apply the
    power to reduce the hp of the target

    :param monster: a dictionary
    :param enemy: a dictionary
    :param move_name: a string
    :precondition: monster is a well-formed dictionary that represents a monster
    :precondition: enemy is a well-formed dictionary that represents an enemy
    :precondition: move_name must be a string referring to a key in the monster dictionary
    :return: updated monster and enemy hp

    >>> test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,'moves': {'ember': {'power': 5, 'accuracy': 80},\
    'scratch': {'power': 3, 'accuracy': 100}},'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}}}
    >>> test_move_name = 'ember'
    >>> use_move(monster, test_enemy, test_move_name) # doctest: +SKIP
    'Ember!'
    'Damage dealt: 5. Remainging HP: 0'
    """
    move = monster['moves'].get(move_name)
    if move and random.randint(1, 100) <= move['accuracy']:
        damage = move['power']
        enemy['hp'] -= damage
        enemy['hp'] = max(0, enemy['hp'])
        text_delay(f"{move_name.capitalize()}!\n")
        text_delay(f"Damage dealt: {damage}. Remaining Target HP: {enemy['hp']}\n")
    else:
        text_delay(f"{move_name.capitalize()}, but it missed!\n")


def is_alive(monster: dict) -> bool:
    """
    Check monster HP

    This function checks if monster current hp is greater than 0

    :param monster: A dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: Check if monster current hp is 0
    :return: True or False
    >>> monster_test = {"x-coordinate": 0, "y-coordinate": 0, "hp": 5}
    >>> is_alive(monster_test)
    True
    >>> monster_test = {"x-coordinate": 0, "y-coordinate": 0, "hp": 0}
    >>> is_alive(monster_test)
    False
    """
    return monster['hp'] > 0


def final_battle(monster: dict, final_boss: dict) -> bool:
    """
    Engage in the final battle between the monster and the final boss.

    :param monster: a dictionary representing the player's monster
    :param final_boss: a dictionary representing the final boss monster
    :precondition: monster is a well-formed dictionaries representing a monster
    :precondition: final_boss is a well-formed dictionary that represents a final boss
    :postcondition: execute the final battle sequence and display a congratulatory message if the player wins
    :return: battle result

    >>>final_battle(monster, final_boss) # doctest: +SKIP
    "Congratulations! Your monster has defeated the final boss and completed its journey!"
    >>>final_battle(monster, final_boss) # doctest: +SKIP
    "Monster has been defeated by the final boss. Better luck next time!"
    """
    make_final_boss()
    text_delay(
        f"Congrats on making it this far, {monster['name']} has {monster['wins']} wins! Time for your final challenge\n")
    result = battle(monster, final_boss)
    if result == f"{monster['name']} wins!\n":
        text_delay("Congratulations! Your monster has defeated the final boss and completed its journey!\n")
        return True
    else:
        text_delay(f"{monster['name']} has been defeated by the final boss. Better luck next time!")
        return False
