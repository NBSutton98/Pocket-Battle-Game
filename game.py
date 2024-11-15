import random

#intro

def make_monster():
    """
    Create a monster.

    :postcondition: create a well-formed dictionary that represents the monster.
    :return: a monster

    >>> make_monster()
    {'wins': 0, 'hp': 20, 'max_hp': 5, 'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'location_x': 0, 'location_y': 0, 'potion_uses': 2}
    """
    monster = {'wins': 0, 'hp': 10, 'max_hp': 10,
        'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'location_x': 0,
        'location_y': 0, 'potion_uses': 2}
    return monster

def make_final_boss():
    """
    Create a final boss.

    :postcondition: create a well-formed dictionary that represents the final boss.
    :return: a monster

    >>> make_final_boss()
    {'hp': 10, 'max_hp': 50, 'moves': {'bite': {'power': 1, 'accuracy': 90}}}
    """
    final_boss = {'hp': 50, 'max_hp': 50, 'moves': {'Big Punch': {'power': 10, 'accuracy': 90}, }}
    return final_boss

def make_enemy():
    """
    Create an enemy.

    :postcondition: create a well-formed dictionary that represents the enemy.
    :return: a monster

    >>> make_enemy()
    {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}}}
    """
    enemy = {'hp': 5, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    return enemy


def potion(monster):
    """
    Heal your monster

    A function that returns your monsters hp to their max hp

    :param monster: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: take monster hp and replace it with the value of the max_hp
    :return: healed monster

    >>> damaged_monster = {'wins': 0, 'hp': 1, 'max_hp': 10, 'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'location_x': 0, 'location_y': 0, 'potion_uses': 2}
    >>> potion(damaged_monster)
    Potion used! Monster's HP restored to max. Potions left: 1
    """
    if monster['potion_uses'] > 0:
        monster['hp'] = monster['max_hp']
        monster['potion_uses'] -= 1
        print(f"Potion used! Monster's HP restored to max. Potions left: {monster['potion_uses']}")
    else:
        print("No potions left to use!")


def evolve(monster, enemy):
    """
    Evolve my monster and enemy

    A function that takes the monster and enemy, raises their max_hp and changes the monsters moves

    :param monster: a dictonary
    :param enemy: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :precondition: enemy is a well-formed dictionary that represents an enemy
    :postcondition: update max hp, change move names and update power of moves
    :return: monster and enemy

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'location_x': 0,'location_y': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    >>> evolve(test_monster, test_enemy)
    Wow! That is 3 wins for your monster! Your monster glows in a white light and begins to evolve
    Monster evolved! Stats and move power increased. They have learned ['flamethrower', 'slash']
    Enemy has grown stronger!
    """
    if monster['wins'] >= 3:
        print(
            f'Wow! That is {monster['wins']} wins for your monster! Your monster glows in a white light and begins to evolve')
        monster['max_hp'] += 10
        monster['hp'] = monster['max_hp']
        monster['moves']['flamethrower'] = monster['moves'].pop('ember')
        monster['moves']['flamethrower']['power'] *= 2
        monster['moves']['slash'] = monster['moves'].pop('scratch')
        monster['moves']['slash']['power'] *= 2
        print(f"Monster evolved! Stats and move power increased. They have learned {list(monster['moves'].keys())}")

        enemy['max_hp'] += 8
        enemy['hp'] = enemy['max_hp']
        for move in enemy['moves']:
            enemy['moves'][move]['power'] += 2
        print("Enemy has grown stronger!")


def evolve_final(monster):
    """
    Evolve monster to final stage

    A function that takes the monster and maxes their stats and learns the most powerful moves!

    :param monster: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: update max hp, change move names and update power of moves
    :return: monster

    >>> test_monster = {'wins': 6, 'hp': 20, 'max_hp': 10,'moves': {'flamethrower': {'power': 10, 'accuracy': 80}, 'slash': {'power': 6, 'accuracy': 100}}, 'location_x': 0,'location_y': 0, 'potion_uses': 2}
    >>> evolve_final(test_monster)
    Wow! That is 6 wins for your monster! Your monster glows in a white light and begins to evolve
    Monster has reached final evolution! Stats and move power have maxed out. They have learned ['fire blast', 'crush']    """
    if monster['wins'] >= 6:
        print(
            f'Wow! That is {monster['wins']} wins for your monster! Your monster glows in a white light and begins to evolve')
        monster['max_hp'] += 10
        monster['hp'] = monster['max_hp']
        monster['moves']['fire blast'] = monster['moves'].pop('flamethrower')
        monster['moves']['fire blast']['power'] *= 2
        monster['moves']['crush'] = monster['moves'].pop('slash')
        monster['moves']['crush']['power'] *= 2
        print(f"Monster has reached final evolution! Stats and move power have maxed out. They have learned {list(monster['moves'].keys())}")



def battle(monster, enemy):
    """
    Simulate battle

    This function takes the monster and enemy dictionaries and allows user input to effect hp using moves and their power

    :param monster: a dictionary
    :param enemy: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :precondition: enemy is a well-formed dictionary that represents an enemy
    :postcondition: take user input to select move names, apply the power value to reduce your hp of opponent
    :return: "Monster Wins!" or "Enemy Wins!"

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'location_x': 0,'location_y': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    >>> battle(test_monster, test_enemy) # doctest: +SKIP
    "Monster wins!"
    """
    print("The battle begins!")
    while monster['hp'] > 0 and enemy['hp'] > 0:
        print("Monster's turn:")
        move_names = list(monster['moves'].keys())
        print(f"1. {move_names[0].capitalize()} (Power: {monster['moves'][move_names[0]]['power']}, Accuracy: {monster['moves'][move_names[0]]['accuracy']}%)")
        print(f"2. {move_names[1].capitalize()} (Power: {monster['moves'][move_names[1]]['power']}, Accuracy: {monster['moves'][move_names[1]]['accuracy']}%)")
        while True:
            move_choice = input("Choose a move (1 or 2): ")
            if move_choice in ["1", "2"]:
                user_move = move_names[int(move_choice) - 1]
                break
            else:
                print("Invalid choice! Please enter '1' or '2'.")
        use_move(monster, enemy, user_move)
        if enemy['hp'] <= 0:
            print("Enemy defeated!")
            monster['wins'] += 1
            enemy['hp'] = enemy['max_hp']
            healing = input("Would you like to heal? '1' yes, '2' no: ")
            while healing not in ['1', '2']:
                print("Invalid choice! Please enter '1' or '2'.")
                healing = input("Would you like to heal? '1' yes, '2' no: ")
            if healing == '1':
                potion(monster)
                return "Monster wins!"
            elif healing == '2':
                print("Continuing without healing.")
                return "Monster wins!"

        enemy_move = 'bite'
        use_move(enemy, monster, enemy_move)

        if monster['hp'] <= 0:
            print("Monster defeated! Sent back to start.")
            monster['hp'] = monster['max_hp']
            return "Enemy wins!"

    print("Battle over!")


def use_move(monster, enemy, move_name):
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
    """
    move = monster['moves'].get(move_name)
    if move and random.randint(1, 100) <= move['accuracy']:
        damage = move['power']
        enemy['hp'] -= damage
        enemy['hp'] = max(0, enemy['hp'])
        print(f"Monster used {move_name.capitalize()}!")
        print(f"Damage dealt: {damage}. Remaining HP: {enemy['hp']}")
    else:
        print(f"Monster used {move_name.capitalize()}, but it missed!")

def final_battle(monster, final_boss):
    """
    Engage in the final battle between the monster and the final boss.

    :param monster: a dictionary representing the player's monster
    :param final_boss: a dictionary representing the final boss monster
    :precondition: monster is a well-formed dictionaries representing a monster
    :precondition: final_boss is a well-formed dictionary that represents a final boss
    :postcondition: execute the final battle sequence and display a congratulatory message if the player wins
    :return: battle result
    """
    print(f"Congrats on making it this far, your has {monster['wins']} wins! Time for your final challenge")
    result = battle(monster, final_boss)
    if result == "Monster wins!":
        print("Congratulations! Your monster has defeated the final boss and completed its journey!")
    else:
        print("Your monster has been defeated by the final boss. Better luck next time!")



