import battle
import board
import characters
import evolve
import movement


def main():
    """Drive the program"""
    movement.intro()
    my_board = board.make_board(5, 5)
    name = input("What is your monster's name?: ")
    monster = characters.make_monster(name)
    enemy = characters.make_enemy()

    while True and battle.is_alive(monster):

        board.describe_current_location(my_board, monster)

        board.display_map(my_board, monster, 5, 5)

        direction = movement.get_user_choice()
        valid_move = movement.validate_move(monster, direction)

        if valid_move:

            movement.move_monster(monster, direction)

            there_is_a_challenger = movement.check_for_foes()
            if there_is_a_challenger:
                battle.battle(monster, enemy)

                if monster['wins'] == 3:
                    evolve.evolve(monster, enemy)
        else:
            print("You can't go that way!")

        if monster['wins'] == 6:
            evolve.evolve_final(monster)
            final_boss = characters.make_final_boss()
            final_battle_result = battle.final_battle(monster, final_boss)

            if final_battle_result:
                print("You have completed your battle simulation test. Thank you for playing!")
                break
            else:
                print("Game over! Your monster has been defeated.")
                break


if __name__ == "__main__":
    main()
