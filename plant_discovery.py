number_of_founded_plants = int(input())

plants_collection = {}

for _ in range(number_of_founded_plants):
    found_plants = input().split("<->")
    plant, rarity = found_plants[0], int(found_plants[1])
    if plant not in plants_collection:
        plants_collection[plant] = {"Rarity": rarity, "Rating": []}

command = input()

while command != "Exhibition":

    command = command.split(": ")
    action = command[0]

    if action == "Rate":
        search = command[1].split(" - ")
        herb = search[0]
        rating = search[1]
        if herb in plants_collection:
            plants_collection[herb]["Rating"].append(int(rating))
        else:
            print("error")


    elif action == "Update":
        search = command[1].split(" - ")
        herb = search[0]
        new_rarity = search[1]
        if herb in plants_collection:
            plants_collection[herb]["Rarity"] = new_rarity
        else:
            print("error")


    elif action == "Reset":
        search = command[1].split(" - ")
        herb = search[0]
        if herb in plants_collection:
            plants_collection[herb]["Rating"] = []
        else:
            print("error")


    command = input()

print("Plants for the exhibition:")
for plant_name in plants_collection.keys():
    if plants_collection[plant_name]["Rating"]:
        average_rating = sum(plants_collection[plant_name]["Rating"]) / len(plants_collection[plant_name]["Rating"])
    else:
        average_rating = 0
    print(f'- {plant_name}; Rarity: {plants_collection[plant_name]["Rarity"]}; Rating: {average_rating:.2f}')
