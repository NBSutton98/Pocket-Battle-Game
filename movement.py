import random
import time


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


def intro():
    text_delay("Thank you for trying my first game, this will be a battle simulation featuring your very own monster, "
               "your objective is, explore,\n"
               "get a total of 6 battle wins and defeat the final challenge, good luck! \n\n")

    text_delay("Well, it is finally time....Go set off on your adventure,\n"
               "but make sure to bring that crazy monster of "
               "yours for protection, umm... what was its name again?\n")
    return


def text_delay(text):
    for letters in text:
        print(letters, end='')
        time.sleep(0.01)
