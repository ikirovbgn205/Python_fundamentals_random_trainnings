def plunder(some_dictionary:dict, any_town:str, some_people:int, some_gold:int)-> dict:
    some_dictionary[any_town]["population"] -= some_people
    some_dictionary[any_town]["gold"] -= some_gold
    print(f"{any_town} plundered! {some_gold} gold stolen, {some_people} citizens killed.")
    if some_dictionary[any_town]["population"] == 0 or some_dictionary[any_town]["gold"] == 0:
        del some_dictionary[any_town]
        print(f"{any_town} has been wiped off the map!")
    return some_dictionary

def main():

    first_command = input()

    cities_dictionary = {}

    while first_command != "Sail":

        city, population, gold = first_command.split("||")

        if city not in cities_dictionary:
            cities_dictionary[city] = {"population": int(population), "gold": int(gold)}

        else:
            cities_dictionary[city]["population"] += int(population)
            cities_dictionary[city]["gold"] += int(gold)

        first_command = input()

    second_command = input()

    while second_command != "End":

        second_command = second_command.split("=>")
        action = second_command[0]

        if action == "Plunder":
            town, people, gold = second_command[1], int(second_command[2]), int(second_command[3])
            cities_dictionary = plunder(cities_dictionary, town, people, gold)

        elif action == "Prosper":
            prosper_town, earned_gold = second_command[1], int(second_command[2])
            if earned_gold > 0:
                cities_dictionary[prosper_town]["gold"] += earned_gold
                total_gold = cities_dictionary[prosper_town]["gold"]
                print(f"{earned_gold} gold added to the city treasury. {prosper_town} now has {total_gold} gold.")
            else:
                print("Gold added cannot be a negative number!")

        second_command = input()

    if cities_dictionary:
        print(f"Ahoy, Captain! There are {len(cities_dictionary)} wealthy settlements to go to:")
        for current_town in cities_dictionary.keys():
            current_population = cities_dictionary[current_town]["population"]
            amount_gold = cities_dictionary[current_town]["gold"]
            print(f"{current_town} -> Population: {current_population} citizens, Gold: {amount_gold} kg")
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")

main()