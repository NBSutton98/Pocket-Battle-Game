from movement import text_delay


def evolve(monster: dict, enemy: dict):
    if monster['wins'] >= 3:
        text_delay(
            f"Wow! That is {monster['wins']} wins for your monster! Your monster glows in a white light and begins to "
            f"evolve\n"
        )
        monster['max_hp'] += 10
        monster['hp'] = monster['max_hp']
        monster['moves']['flamethrower'] = monster['moves'].pop('ember')
        monster['moves']['flamethrower']['power'] *= 2
        monster['moves']['slash'] = monster['moves'].pop('scratch')
        monster['moves']['slash']['power'] *= 2
        text_delay(
            f"{monster['name']} evolved! Stats increased. They have learned {list(monster['moves'].keys())}\n"
        )
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

    >>> test_monster = {'name': 'nick', 'wins': 6, 'hp': 20, 'max_hp': 10,\
    'moves': {'flamethrower': {'power': 10, 'accuracy': 80},'slash': {'power': 2, 'accuracy': 100}}}
    >>> evolve_final(test_monster)
    Wow! That is 6 wins for nick! Your monster glows in a white light and begins to evolve
    nick has reached final evolution! Stats and move power have maxed out. They have learned ['fire blast', 'crush']
    >>> test_monster = {'name': 'nick', 'wins': 5, 'hp': 20, 'max_hp': 10,\
    'moves': {'flamethrower': {'power': 10, 'accuracy': 80},'slash': {'power': 2, 'accuracy': 100}}}
    >>> evolve_final(test_monster)
    """
    if monster['wins'] >= 6:
        text_delay(
            f'Wow! That is {monster['wins']} wins for {monster['name']}! Your monster glows in a white light and '
            f'begins to'
            f' evolve')
        monster['max_hp'] += 20
        monster['hp'] = monster['max_hp']
        monster['moves']['fire blast'] = monster['moves'].pop('flamethrower')
        monster['moves']['fire blast']['power'] *= 2
        monster['moves']['crush'] = monster['moves'].pop('slash')
        monster['moves']['crush']['power'] *= 2
        print(
            f"{monster['name']} has reached final evolution! Stats and move power have maxed out. They have learned"
            f" {list(monster['moves'].keys())}\n\n")
