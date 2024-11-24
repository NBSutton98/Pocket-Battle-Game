import random
import itertools


def intro():
    print("Thank you for trying my first game, this will be a battle simulation featuring your very own monster, "
          "your objective is to get a total of 6 battle wins and defeat the final challenge, good luck! ")
    print("Well, it is finally time....Go set off on your adventure, but make sure to bring that crazy monster of "
          "yours for protection, umm... what was its name again?")


def make_monster(name) -> dict:
    """
    Create a monster.

    :postcondition: create a well-formed dictionary that represents the monster.
    :return: a monster

    >>> make_monster() {'name':name 'wins': 0, 'hp': 10, 'max_hp': 10, 'moves': {'ember': {'power': 5, 'accuracy': 80},
    'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
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

    >>> make_final_boss()
    {'hp': 10, 'max_hp': 50, 'moves': {'bite': {'power': 1, 'accuracy': 90}}}
    """
    final_boss = {'hp': 50, 'max_hp': 50, 'name': 'Skibidi',
                  'moves': {'big punch': {'power': 10, 'accuracy': 90}, 'hyper beam': {'power': 15, 'accuracy': 100}}}
    return final_boss


def make_enemy() -> dict:
    """
    Create an enemy.

    :postcondition: create a well-formed dictionary that represents the enemy.
    :return: a monster

    >>> make_enemy()
    {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}}}
    """
    enemy = {'hp': 5, 'max_hp': 5, "name": "Pidgey",
             'moves': {'bite': {'power': 2, 'accuracy': 100}, 'punch': {'power': 1, 'accuracy': 100}}}
    return enemy


def potion(monster: dict):
    """
    Heal your monster

    A function that returns your monsters hp to their max hp

    :param monster: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: take monster hp and replace it with the value of the max_hp
    :return: healed monster

    >>> damaged_monster = {'wins': 0, 'hp': 1, 'max_hp': 10, 'moves': {'ember': {'power': 5, 'accuracy': 80},
    'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> potion(damaged_monster)
    Potion used! Monster's HP restored to max. Potions left: 1
    """
    if monster['potion_uses'] > 0:
        monster['hp'] = monster['max_hp']
        monster['potion_uses'] -= 1
        print(f"Potion used! {monster['name']}s HP restored to max. Potions left: {monster['potion_uses']}")
    else:
        print("No potions left to use!")


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
    {'hp': 10, 'max_hp': 10}
    """
    while True:
        healing = input(f"Would you like to heal? Current HP:{monster['hp']} '1' yes, '2' no: ")
        if healing in ["1", "2"]:
            if healing == '1':
                potion(monster)
                return f"{monster['name']} wins!"
            elif healing == '2':
                print("Continuing without healing.")
                return f"{monster['name']} wins!"
        else:
            print("Invalid choice! Please enter '1' or '2'.")


def evolve(monster: dict, enemy: dict):
    """
    Evolve my monster and enemy

    A function that takes the monster and enemy, raises their max_hp and changes the monsters moves

    :param monster: a dictonary
    :param enemy: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :precondition: enemy is a well-formed dictionary that represents an enemy
    :postcondition: update max hp, change move names and update power of moves
    :return: monster and enemy

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80},
     'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    >>> evolve(test_monster, test_enemy)
    Wow! That is 3 wins for your monster! Your monster glows in a white light and begins to evolve
    Monster evolved! Stats and move power increased. They have learned ['flamethrower', 'slash']
    Enemy has grown stronger!
    """
    if monster['wins'] >= 3:
        print(
            f'Wow! That is {monster['wins']} wins for your monster! Your monster glows in a white light and begins '
            f'to evolve')
        monster['max_hp'] += 10
        monster['hp'] = monster['max_hp']
        monster['moves']['flamethrower'] = monster['moves'].pop('ember')
        monster['moves']['flamethrower']['power'] *= 2
        monster['moves']['slash'] = monster['moves'].pop('scratch')
        monster['moves']['slash']['power'] *= 2
        print(
            f"{monster['name']} evolved! Stats and move power increased. They have learned {list(monster['moves'].keys())}")

        enemy['max_hp'] += 8
        enemy['hp'] = enemy['max_hp']
        enemy['moves'] = {move: {'power': data['power'] + 2, 'accuracy': data['accuracy']} for move, data in
                          enemy['moves'].items()}
        enemy['name'] = 'Balloonist'
        print(f"Your enemy has evolved into, {enemy['name']}")


def evolve_final(monster: dict):
    """
    Evolve monster to final stage

    A function that takes the monster and maxes their stats and learns the most powerful moves!

    :param monster: a dictonary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: update max hp, change move names and update power of moves
    :return: monster

    >>> test_monster = {'wins': 6, 'hp': 20, 'max_hp': 10,'moves': {'flamethrower': {'power': 10, 'accuracy': 80},
     'slash': {'power': 6, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> evolve_final(test_monster)
    Wow! That is 6 wins for your monster! Your monster glows in a white light and begins to evolve
    Monster has reached final evolution! Stats and move power have maxed out. They have learned ['fire blast', 'crush']
    """
    if monster['wins'] >= 6:
        print(
            f'Wow! That is {monster['wins']} wins for {monster['name']}! Your monster glows in a white light and '
            f'begins to'
            f' evolve')
        monster['max_hp'] += 10
        monster['hp'] = monster['max_hp']
        monster['moves']['fire blast'] = monster['moves'].pop('flamethrower')
        monster['moves']['fire blast']['power'] *= 2
        monster['moves']['crush'] = monster['moves'].pop('slash')
        monster['moves']['crush']['power'] *= 2
        print(
            f"{monster['name']} has reached final evolution! Stats and move power have maxed out. They have learned"
            f" {list(monster['moves'].keys())}")


def move_choice(monster: dict) -> str:
    """
    Select monster move

    This function accesses the monster move dictionary and prompts the user to select one of 2 the moves,
    preventing any other input

    :param monster: a dictionary
    :precondition: monster is a well-formed dictionary that represents a monster
    :postcondition: get user input and access monster moves, if move exists otherwise get user input
    :return: monster move

    >>>test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,'moves': {'ember': {'power': 5, 'accuracy': 80},
     'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2} # doctest: +SKIP
    >>>move_choice(monster) # doctest: +SKIP
    'ember'
    """
    while True:
        move_names = list(monster['moves'].keys())
        print(
            f"1. {move_names[0].capitalize()} (Power: {monster['moves'][move_names[0]]['power']},"
            f" Accuracy: {monster['moves'][move_names[0]]['accuracy']}%)")
        print(
            f"2. {move_names[1].capitalize()} (Power: {monster['moves'][move_names[1]]['power']},"
            f" Accuracy: {monster['moves'][move_names[1]]['accuracy']}%)")
        move_input = input("Choose a move (1 or 2): ")
        if move_input in ["1", "2"]:
            user_move = move_names[int(move_input) - 1]
            return user_move
        else:
            print("Invalid choice! Please enter '1' or '2'.")


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

    >>> test_monster = {'wins': 3, 'hp': 20, 'max_hp': 5,'moves': {'ember': {'power': 5, 'accuracy': 80},
     'scratch': {'power': 3, 'accuracy': 100}}, 'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>> test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}, }}
    >>> battle(test_monster, test_enemy) # doctest: +SKIP
    "Monster wins!"
    """
    enemy_move_cycle = itertools.cycle(enemy['moves'])
    print("The battle begins!")
    while is_alive(monster):
        print(f"{monster['name']} turn:")
        move = move_choice(monster)
        use_move(monster, enemy, move)
        if enemy['hp'] <= 0:
            print(f"{enemy['name']} defeated!")
            monster['wins'] += 1
            enemy['hp'] = enemy['max_hp']
            use_potion(monster)
            return f"{monster['name']} wins!"
        print(f"{enemy['name']} turn:")
        enemy_move = next(enemy_move_cycle)
        use_move(enemy, monster, enemy_move)
        if monster['hp'] <= 0:
            print("Monster defeated! Sent back to start.")
            return "Enemy wins!"

    print("Battle over!")


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
    """
    return monster['hp'] > 0


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

    >>>test_monster = {'wins': 0, 'hp': 5, 'max_hp': 10,'moves': {'ember': {'power': 5, 'accuracy': 80},
     'scratch': {'power': 3, 'accuracy': 100}},'x-coordinate': 0, 'y-coordinate': 0, 'potion_uses': 2}
    >>>test_enemy = {'hp': 10, 'max_hp': 5, 'moves': {'bite': {'power': 1, 'accuracy': 90}}}
    >>>test_move_name = 'ember'
    >>>use_move(monster, test_enemy, test_move_name) # doctest: +SKIP
    'Ember!'
    'Damage dealt: 5. Remainging HP: 0'
    """
    move = monster['moves'].get(move_name)
    if move and random.randint(1, 100) <= move['accuracy']:
        damage = move['power']
        enemy['hp'] -= damage
        enemy['hp'] = max(0, enemy['hp'])
        print(f"{move_name.capitalize()}!")
        print(f"Damage dealt: {damage}. Remaining Target HP: {enemy['hp']}")
    else:
        print(f"{move_name.capitalize()}, but it missed!")


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
    """
    make_final_boss()
    print(
        f"Congrats on making it this far, {monster['name']} has {monster['wins']} wins! Time for your final challenge")
    result = battle(monster, final_boss)
    if result == f"{monster['name']} wins!":
        print("Congratulations! Your monster has defeated the final boss and completed its journey!")
        return True
    else:
        print(f"{monster['name']} has been defeated by the final boss. Better luck next time!")
        return False


def make_board(rows: int, columns: int) -> dict:
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
    room_descriptions = ["A lush garden courtyard buzzing with glowing fireflies and vibrant flowers.",
                         "A mystical cave glimmering with crystal formations and hidden pools.",
                         "A serene beachside shack with the sound of waves crashing nearby.",
                         "A shadowy forest clearing lit by bioluminescent plants and the soft hoot of owls.",
                         "A bustling marketplace filled with exotic spices, trinkets, and lively chatter.",
                         "A hidden library with dusty tomes, secret passageways, and a faint smell of parchment.",
                         "A windswept cliffside with a lone lighthouse overlooking the vast ocean.",
                         "An ancient temple with intricate carvings and flickering torches along the walls.",
                         "A foggy swamp with twisted trees and mysterious glowing eyes watching from the dark.",
                         "A magical treehouse perched high in the canopy, connected by rope bridges.",
                         "A quaint village square with cobblestone streets and cozy cottages.",
                         "A sunlit meadow dotted with colorful wildflowers and gently grazing creatures.",
                         "An eerie castle dungeon with cold stone walls and faint echoes of dripping water.",
                         "A vibrant carnival with spinning rides, cheerful music, and the smell of cotton candy.",
                         "A frozen tundra with sparkling icicles, crunching snow, and the howling wind.",
                         "A serene waterfall cave with shimmering rainbows and soft moss underfoot.",
                         "A mysterious underground laboratory with bubbling beakers and glowing monitors.",
                         "A cozy inn with a roaring fire, soft chairs, and the hum of cheerful conversation.",
                         "A treetop sanctuary with hanging lanterns and the rustling of leaves in the breeze.",
                         "A windswept desert oasis with crystal-clear water and swaying palm trees.",
                         "A stormy mountain peak with jagged rocks, swirling mist, and the roar of thunder.",
                         "An abandoned train station with overgrown tracks and a faint, haunting whistle.",
                         "A peaceful shrine nestled within a bamboo grove, its air filled with incense.",
                         "A cavernous mine with tracks leading to deep, shadowy tunnels.",
                         "A moonlit cliff surrounded by glowing mushrooms and soft whispers on the wind."]

    board = {}
    for row in range(rows):
        for column in range(columns):
            board[(row, column)] = random.choice(room_descriptions)
    return board


def describe_current_location(board: dict, monster: dict):
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


def validate_move(monster: dict, direction: str) -> bool:
    """
    Validate user movement

    This function takes the users directional input and checks that it is within the bounds
    of the board

    :param monster: A dictionary
    :param direction: A string
    :precondition: monster is a well-formed dictionary that represents a monster    and current HP
    :precondition direction: A one letter string consisting of 'w', 's', 'd' or 'a'
    :postcondition: Take the monster x and y coordinates and check to make sure it is within the bounds of the board
    :return: Boolean

    >>> monster_test = {"x-coordinate": 0, "y-coordinate": 0, "current_hp": 5}
    >>> test_direction = 's'
    >>> validate_move(monster_test, test_direction)
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


def move_monster(monster: dict, direction: str) -> bool:
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
    name = input("What is your monsters name?: ")
    monster = make_monster(name)
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
