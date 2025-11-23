def cast_spell(some_dict:dict, some_command:list) -> dict:
    hero, mana_needed, spell_name = some_command[1], int(some_command[2]), some_command[3]
    if some_dict[hero]['MP'] > mana_needed:
        some_dict[hero]['MP'] -= mana_needed
        print(f"{hero} has successfully cast {spell_name} and now has {some_dict[hero]['MP']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")
    return some_dict

def take_damage(some_dict:dict, some_command:list) -> dict:
    hero, damage, attacker = some_command[1], int(some_command[2]), some_command[3]
    some_dict[hero]['HP'] -= damage
    if some_dict[hero]['HP'] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {some_dict[hero]['HP']} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del some_dict[hero]
    return some_dict


def recharge(some_dict:dict, some_command:list) -> dict:
    hero, amount = some_command[1], int(some_command[2])
    amount_recovered = amount
    some_dict[hero]['MP'] += amount
    if some_dict[hero]['MP'] > 200:
        amount_recovered = amount - (some_dict[hero]['MP'] - 200)
        some_dict[hero]['MP'] = 200
    print(f"{hero} recharged for {amount_recovered} MP!")
    return some_dict


def heal(some_dict:dict, some_command:list) -> dict:
    hero, amount = some_command[1], int(some_command[2])
    other_amount_recovered = amount
    some_dict[hero]['HP'] += amount
    if some_dict[hero]['HP'] > 100:
        other_amount_recovered = amount - (some_dict[hero]['HP'] - 100)
        some_dict[hero]['HP'] = 100
    print(f"{hero} healed for {other_amount_recovered} HP!")
    return some_dict


number_of_heroes = int(input())

dictionary_of_heroes = {}

for hero in range(number_of_heroes):
    command = input()
    hero_name, health_points, mana_points = command.split(' ')
    dictionary_of_heroes[hero_name] = {"HP": int(health_points), "MP": int(mana_points)}

command_two = input()

while command_two != "End":
    command_two = command_two.split(' - ')
    action = command_two[0]

    if action == "CastSpell":
        dictionary_of_heroes = cast_spell(dictionary_of_heroes, command_two)

    elif action == "TakeDamage":
        dictionary_of_heroes = take_damage(dictionary_of_heroes, command_two)

    elif action == "Recharge":
        dictionary_of_heroes = recharge(dictionary_of_heroes, command_two)

    elif action == "Heal":
        dictionary_of_heroes = heal(dictionary_of_heroes, command_two)

    command_two = input()

for hero, points in dictionary_of_heroes.items():
    print(f"{hero}")
    print(f' HP: {points["HP"]}')
    print(f' MP: {points["MP"]}')