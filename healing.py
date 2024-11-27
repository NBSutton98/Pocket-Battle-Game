from movement import text_delay


def potion(monster: dict):
    """
    Heal your monster

    A function that returns your monsters hp to their max hp

    :param monster: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: take monster hp and replace it with the value of the max_hp
    :return: healed monster

    >>> damaged_monster = {'name': 'nick', 'wins': 0, 'hp': 1, 'max_hp': 10, \
    'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, \
    'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> potion(damaged_monster)
    Potion used! nicks HP restored to max. Potions left: 1
    """
    if monster['potion_uses'] > 0:
        monster['hp'] = monster['max_hp']
        monster['potion_uses'] -= 1
        text_delay(f"Potion used!\n {monster['name']}s HP restored to max. Potions left: {monster['potion_uses']}\n")
    else:
        text_delay("No potions left to use!\n")


def use_potion(monster: dict) -> str:
    """
    Heal monster

    A simple function that ask the user if they would like to heal their monster.

    :param monster: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: apply potion function to monster or not
    :return: monster
    >>> test_monster = {'hp': 1, 'max_hp': 10} # doctest: +SKIP
    >>>use_potion(test_monster) # doctest: +SKIP
    >>> test_monster2 = {'hp': 10, 'max_hp': 10} # doctest: +SKIP
    >>>use_potion(test_monster) # doctest: +SKIP
    {'hp': 10, 'max_hp': 10}
    """
    while True:
        healing = input(f"Would you like to heal?\n Current HP:{monster['hp']}\n '1' yes, '2' no: ")
        if healing in ["1", "2"]:
            if healing == '1':
                potion(monster)
                return f"{monster['name']} wins!"
            elif healing == '2':
                text_delay("Continuing without healing.\n")
                return f"{monster['name']} wins!"
        else:
            text_delay("Invalid choice! Please enter '1' or '2'.")
