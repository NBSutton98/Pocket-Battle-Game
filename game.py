def make_monster():
    monster  = {
            'wins': 0,
            'hp': 20,
            'max_hp': 5,
            'moves': { 'ember': {'power': 2, 'accuracy': 80}, 'scratch': {'power': 1, 'accuracy': 100} },
            'location_x': 0,
            'location_y': 0,
            'potion_uses': 2
            }
    return monster

def make_enemy():
   enemy = {
        'hp': 10,
        'max_hp': 5,
        'moves':{'bite': {'power': 1, 'accuracy': 90},
        }
   }
   return enemy



def potion(monster):
    if monster['potion_uses'] > 0:
        monster['hp'] = monster['max_hp']
        monster['potion_uses'] -= 1
        print(f"Potion used! Monster's HP restored to max. Potions left: {monster['potion_uses']}")
    else:
        print("No potions left to use!")

def use_move(attacker, defender, move_name):
def fight(enemy, monster):
def win_fight(enemy, monster):
def lose_fight(enemy, monster):
def evolve_two(enemy, monster):
def final_battle(enemy, monster):


def evolve_one(enemy, monster):
    if monster['wins'] >= 3:
        print(f'Wow! That is {monster['wins']} wins for your monster! Your monster glows in a white light and begins to evolve')
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
            enemy['moves'][move]['power'] += 1

        print("Enemy has grown stronger!")




