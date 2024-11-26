from characters import make_monster
import random


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
                         "A serene beach side shack with the sound of waves crashing nearby.",
                         "A shadowy forest clearing lit by bioluminescent plants and the soft hoot of owls.",
                         "A bustling marketplace filled with exotic spices, trinkets, and lively chatter.",
                         "A hidden library with dusty tomes, secret passageways, and a faint smell of parchment.",
                         "A windswept cliff side with a lone lighthouse overlooking the vast ocean.",
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


def display_map(board: dict, monster: dict, rows: int, columns: int):
    """
    Display a 2D map showing the monster's current location.

    :param board: A dictionary representing the game board with coordinates as keys.
    :param monster: A dictionary representing the monster, containing its current coordinates.
    :param rows: An integer representing the number of rows in the board.
    :param columns: An integer representing the number of columns in the board.
    :precondition: board must be a valid dictionary with coordinates as keys.
    :precondition: monster must be a dictionary with "x-coordinate" and "y-coordinate".
    :precondition: rows and columns must be positive integers matching the board's dimensions.
    :postcondition: Prints a 2D map showing the monster location using X and -
    :return: 2D map
    """
    monster_location = (monster["x-coordinate"], monster["y-coordinate"])

    for row in range(rows):
        row_display = []
        for column in range(columns):
            if (row, column) == monster_location:
                row_display.append("X")
            else:
                row_display.append("-")
        print(" ".join(row_display))
    print()
