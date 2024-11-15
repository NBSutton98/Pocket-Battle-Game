import random


def intro():
    print("welcome to this place")
    print("this is how you play")


def make_monster():
    """
    Create a monster.

    :postcondition: create a well-formed dictionary that represents the monster.
    :return: a monster

    >>> make_monster()
    {'wins': 0, 'hp': 2, 'max_hp': 10, 'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    """
    monster = {'wins': 0, 'hp': 5, 'max_hp': 10,
               'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}},
               'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
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

    >>> damaged_monster = {'wins': 0, 'hp': 1, 'max_hp': 10, 'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> potion(damaged_monster)
    Potion used! Monster's HP restored to max. Potions left: 1
    """
    if monster['potion_uses'] > 0:
        monster['hp'] = monster['max_hp']
        monster['potion_uses'] -= 1
        print(f"Potion used! Monster's HP restored to max. Potions left: {monster['potion_uses']}")
    else:
        print("No potions left to use!")


def use_potion(monster):
    """
    Heal monster

    A simple function that ask the user if they would like to heal their monster.

    :param monster: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: apply potion function to monster or not
    :return: monster
    >>> test_monster = {'hp': 1, 'max_hp': 10} # doctest: +SKIP
    >>>use_potion(test_monster) # doctest: +SKIP
    {'hp': 10, 'max_hp': 10}
    """
    while True:
        healing = input(f"Would you like to heal? Current HP:{monster['hp']} '1' yes, '2' no: ")
        if healing in ["1", "2"]:
            if healing == '1':
                potion(monster)
                return "Monster wins!"
            elif healing == '2':
                print("Continuing without healing.")
                return "Monster wins!"
        else:
            print("Invalid choice! Please enter '1' or '2'.")


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

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
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
        enemy['moves'] = {move: {'power': data['power'] + 2, 'accuracy': data['accuracy']} for move, data in
                          enemy['moves'].items()}
        print("Enemy has grown stronger!")


def evolve_final(monster):
    """
    Evolve monster to final stage

    A function that takes the monster and maxes their stats and learns the most powerful moves!

    :param monster: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: update max hp, change move names and update power of moves
    :return: monster

    >>> test_monster = {'wins': 6, 'hp': 20, 'max_hp': 10,'moves': {'flamethrower': {'power': 10, 'accuracy': 80}, 'slash': {'power': 6, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
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
        print(
            f"Monster has reached final evolution! Stats and move power have maxed out. They have learned {list(monster['moves'].keys())}")


def move_choice(monster):
    """
    Select monster move

    This function accesses the monster move dictionary and prompts the user to select one of 2 the moves,
    preventing any other input

    :param monster: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: get user input and access monster moves, if move exists otherwise get user input
    :return: monster move

    >>>test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2} # doctest: +SKIP
    >>>move_choice(monster) # doctest: +SKIP
    'ember'
    """
    while True:
        move_names = list(monster['moves'].keys())
        print(
            f"1. {move_names[0].capitalize()} (Power: {monster['moves'][move_names[0]]['power']}, Accuracy: {monster['moves'][move_names[0]]['accuracy']}%)")
        print(
            f"2. {move_names[1].capitalize()} (Power: {monster['moves'][move_names[1]]['power']}, Accuracy: {monster['moves'][move_names[1]]['accuracy']}%)")
        move_input = input("Choose a move (1 or 2): ")
        if move_input in ["1", "2"]:
            user_move = move_names[int(move_input) - 1]
            return user_move
        else:
            print("Invalid choice! Please enter '1' or '2'.")


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

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80}, 'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    >>> battle(test_monster, test_enemy) # doctest: +SKIP
    "Monster wins!"
    """
    print("The battle begins!")
    while is_alive(monster):
        print("Monster's turn:")
        move = move_choice(monster)
        use_move(monster, enemy, move)
        if enemy['hp'] <= 0:
            print("Enemy defeated!")
            monster['wins'] += 1
            enemy['hp'] = enemy['max_hp']
            use_potion(monster)
            return "Monster wins!"
        print("enemy's turn:")
        enemy_move = next(iter(enemy['moves']))
        use_move(monster, enemy, enemy_move)

        if monster['hp'] <= 0:
            print("Monster defeated! Sent back to start.")
            return "Enemy wins!"

    print("Battle over!")


def is_alive(monster):
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
    """
    return monster['hp'] > 0


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
        print(f"{move_name.capitalize()}!")
        print(f"Damage dealt: {damage}. Remaining HP: {enemy['hp']}")
    else:
        print(f"{move_name.capitalize()}, but it missed!")


def final_battle(monster, final_boss):
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
    """
    make_final_boss()
    print(f"Congrats on making it this far, your has {monster['wins']} wins! Time for your final challenge")
    result = battle(monster, final_boss)
    if result == "Monster wins!":
        print("Congratulations! Your monster has defeated the final boss and completed its journey!")
        return True
    else:
        print("Your monster has been defeated by the final boss. Better luck next time!")
        return False


def make_board(rows, columns):
    """
    Create a Grid

    A function that generates a 2-dimensional grid of a desired length and height with each space containing
    a tuple representing x, y coordinates

    :param rows: an integer representing the number of rows
    :param columns: an integer representing the number of columns
    :precondition: rows must be a positive non-zero integer
    :precondition: columns must be positive non-zero integers
    :postcondition: generate a grid of length rows and height columns
    :return: Board as a dictionary

    >>> make_board(1, 1) # doctest: +SKIP
    {'0, 0': "A cozy studio with a warm fireplace and vintage decor.", '0, 1': "A sunlit bedroom with pastel walls and a
     plush queen-sized bed.", '1, 0': "A sunlit bedroom with pastel walls", '1, 1': "A spacious attic converted into a
     relaxing reading nook."}
    """
    room_descriptions = ["A cozy studio with a warm fireplace and vintage decor.",
                         "A sunlit bedroom with pastel walls and a plush queen-sized bed.",
                         "An elegant dining room featuring a marble table and crystal chandelier.",
                         "A modern kitchen equipped with stainless steel appliances and a breakfast bar.",
                         "A rustic cabin living room adorned with log furniture and a stone hearth.",
                         "A serene home office with a large window and minimalist design.",
                         "A colorful child's playroom filled with toys and whimsical murals.",
                         "A tranquil bathroom with a soaking tub and soft candlelight.",
                         "A spacious attic converted into a relaxing reading nook.",
                         "A chic apartment balcony with potted plants and a bistro table.",
                         "A luxurious master suite with a private balcony and en-suite bathroom.",
                         "A bohemian living space with rich textiles and eclectic art.",
                         "An airy guest room with soft linens and a view of the garden.",
                         "A sleek modern bathroom with a glass shower and floating vanity.",
                         "A classic library with built-in bookshelves and a comfortable armchair.",
                         "An artistic studio filled with canvases, brushes, and vibrant colors.",
                         "A stylish entryway featuring a large mirror and unique lighting.",
                         "A cozy den with a sectional sofa and a large screen for movie nights.",
                         "A minimalist bedroom with a low platform bed and serene color palette.",
                         "A charming breakfast nook bathed in morning sunlight.",
                         "An inviting family room with a game table and comfortable seating.",
                         "A sophisticated office with dark wood furnishings and a vintage desk.",
                         "A cheerful kitchen with colorful accents and a farmhouse sink.",
                         "A tranquil meditation room with soft cushions and calming decor.",
                         "A spacious laundry room with organized shelves and a utility sink.",
                         "A cozy corner in the basement with a plush rug and soft lighting."]

    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice(room_descriptions)
    return board


def describe_current_location(board, monster):
    """
    Describe the current location of the monster

    Takes the x and y coordinate location of the monster and prints the description of the location at
    that coordinate in relaation to make_board dictonary.

    :param board: A dictionary
    :param monster: A dictionary
    :precondition board: Board must be a dictionary consisting of a tuple of x and y coordinates and a room descriptions
    :precondition monster: monster is a well-formed dictionary that represents a monster
    :postcondition: Print a string from the make_board function that is associated with the x and y coordinates of the
    monster
    :return: A string describing the location of the monster

    >>> board_test = make_board(1, 1)
    >>> monster_test = make_monster()
    >>> describe_current_location(board, monster) # doctest: +SKIP
    "A cozy studio with a warm fireplace and vintage decor."
    """
    monster_location = (monster["x-coordinate"], monster["y-coordinate"])
    room_description = board.get(monster_location)
    print(f"You are currently at coordinates {monster_location}.")
    print(f"Description: {room_description}")
    return room_description


def get_user_choice():
    """
    Get user choice of movement

    This function asks the user to choose a direction to move represented by w(up), s(down), d(right), or a(left)

    :return: User Choice
    >>> get_user_choice()  # doctest: +SKIP
    "W"
    """
    movement = ['w', 's', 'd', 'a']
    print('Choose a direction, W:UP, S:DOWN, D:RIGHT, A:LEFT')
    while True:
        direction = input("What direction would you like to go: ").lower().strip()
        if direction in movement:
            return direction
        else:
            print("That's not a valid direction.")


def validate_move(monster, direction):
    """
    Validate user movement

    This function takes the users directional input and checks that it is within the bounds
    of the board

    :param monster: A dictionary
    :param direction: A string
    :precondition character: A dictionary that must have three key:value pairs representing x and y coordinates
    and current HP
    :precondition direction: A one letter string consisting of 'w', 's', 'd' or 'a'
    :postcondition: Take the character's x/y coordinates and check to make sure it is within the bounds of the board
    :return: Boolean

    >>> character_test = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
    >>> test_direction = 's'
    >>> validate_move(character_test, test_direction)
    True
    """

    x = monster["x-coordinate"]
    y = monster["y-coordinate"]

    if direction == "w":
        new_y = y - 1
        new_x = x
    elif direction == "s":
        new_y = y + 1
        new_x = x
    elif direction == "d":
        new_x = x + 1
        new_y = y
    elif direction == "a":
        new_x = x - 1
        new_y = y
    else:
        return False

    if 0 <= new_x < 5 and 0 <= new_y < 5:
        return True
    else:
        return False


def move_monster(monster, direction):
    """
    Move the monster

    This function modifies the monsters x and y coordinates

    :param monster: a dictionary
    :param direction: a single letter string
    :precondition monster: monster is a well-formed dictionary that represents a monster
    :precondition: direction must be one letter string consisting of 'w', 's', 'd' or 'a'
    :postcondition: adjust the monster's x and y coordinates
    :return: True if the move was successful, False otherwise

    >>> monster_test = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
    >>> test_direction = 's'
    >>> move_monster(monster_test, test_direction)
    True
      >>> print(monster_test)
    {'x-coordinate': 0, 'y-coordinate': 1, 'current_hp': 5}
    """

    if direction == "w":
        monster['y-coordinate'] -= 1
    elif direction == "s":
        monster['y-coordinate'] += 1
    elif direction == "d":
        monster['x-coordinate'] += 1
    elif direction == "a":
        monster['x-coordinate'] -= 1
    else:
        return False

    return True


def check_for_foes():
    """
    Check for a foe

    This function sets a 50% chance of running into a foe after each monster movement

    :return: a Boolean
    >>> check_for_foes() # doctest: +SKIP
    True
    >>> check_for_foes() # doctest: +SKIP
    False
    """
    choice = random.randint(1, 2)
    if choice == 1:
        return True
    else:
        return False


def main():
    intro()
    board = make_board(5, 5)
    monster = make_monster()
    enemy = make_enemy()

    while True and is_alive(monster):
        describe_current_location(board, monster)
        direction = get_user_choice()
        valid_move = validate_move(monster, direction)

        if valid_move:
            move_monster(monster, direction)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                battle(monster, enemy)
                if monster['wins'] == 3:
                    evolve(monster, enemy)
        else:
            print("You Cant Go That Way!")

        if monster['wins'] == 6:
            evolve_final(monster)
            final_boss = make_final_boss()
            final_battle_result = final_battle(monster, final_boss)
            if final_battle_result:
                print("You have completed your journey!")
                break
            else:
                print("Game over! Your monster has been defeated.")
                break


if __name__ == "__main__":
    main()
