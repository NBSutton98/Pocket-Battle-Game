def make_monster(name: str) -> dict:
    """
    Create a monster.

    :postcondition: create a well-formed dictionary that represents the monster.
    :return: a monster+

    >>> make_monster('nick')  # doctest: +NORMALIZE_WHITESPACE
    {'name': 'nick', 'wins': 0, 'hp': 10, 'max_hp': 10, 'moves': {'ember': {'power': 3, 'accuracy': 80},
     'scratch': {'power': 2, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    """
    monster = {'name': name, 'wins': 0, 'hp': 10, 'max_hp': 10,
               'moves': {'ember': {'power': 3, 'accuracy': 80}, 'scratch': {'power': 2, 'accuracy': 100}},
               'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    return monster


def make_final_boss() -> dict:
    """
    Create a final boss.

    :postcondition: create a well-formed dictionary that represents the final boss.
    :return: a monster

    >>> make_final_boss()  # doctest: +NORMALIZE_WHITESPACE
    {'hp': 50, 'max_hp': 50, 'name': 'Skibidi', 'moves': {'big punch': {'power': 10, 'accuracy': 90},
    'hyper beam': {'power': 15, 'accuracy': 100}}}
    """
    final_boss = {'hp': 30, 'max_hp': 26, 'name': 'Skibidi',
                  'moves': {'big punch': {'power': 10, 'accuracy': 90}, 'hyper beam': {'power': 15, 'accuracy': 100}}}
    return final_boss


def make_enemy() -> dict:
    """
    Create an enemy.

    :postcondition: create a well-formed dictionary that represents the enemy.
    :return: a monster

    >>> make_enemy()# doctest: +NORMALIZE_WHITESPACE
    {'hp': 5, 'max_hp': 5, 'name': 'Pidgey', 'moves': {'bite': {'power': 2, 'accuracy': 100},
     'punch': {'power': 1, 'accuracy': 100}}}
    """
    enemy = {'hp': 5, 'max_hp': 5, "name": "Pidgey",
             'moves': {'bite': {'power': 2, 'accuracy': 100}, 'punch': {'power': 1, 'accuracy': 100}}}
    return enemy
