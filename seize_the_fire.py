levels_and_fire = input().split("#")

amount_of_water = int(input())

total_fires_seized = 0

list_of_seized_fires = []

for objects in levels_and_fire:
    level, fire = objects.split(" = ")

    if level == "High":
        if amount_of_water >= int(fire):
            if 81 <= int(fire) <= 125:
                amount_of_water -= int(fire)
                total_fires_seized += int(fire)
                list_of_seized_fires.append(fire)

    elif level == "Medium":
        if amount_of_water >= int(fire):
            if 51 <= int(fire) <= 80:
                amount_of_water -= int(fire)
                total_fires_seized += int(fire)
                list_of_seized_fires.append(fire)

    elif level == "Low":
        if amount_of_water >= int(fire):
            if 1 <= int(fire) <= 50:
                amount_of_water -= int(fire)
                total_fires_seized += int(fire)
                list_of_seized_fires.append(fire)

effort = total_fires_seized * 0.25

print("Cells:")
for cell in list_of_seized_fires:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fires_seized}")