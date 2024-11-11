def monster_start():
    monster_level_one  = {
            'level': 0,
            'hp': 5,
            'max_hp': 5,
            'moves': { 'ember': 2, 'scratch': 1 },
            'location_x': 0,
            'location_y': 0,
            'potion_uses': 2
            }
    return monster_level_one



def potion(monster_level_one):
    if monster_level_one['potion_uses'] > 0:
        monster_level_one['hp'] = monster_start['max_hp']
        monster_level_one['potion_uses'] -= 1
        print(f"Potion used! Monster's HP restored to max. Potions left: {monster_level_one['potion_uses']}")
    else:
        print("No potions left to use!")


