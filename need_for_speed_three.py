def drive(cars_collection:dict, any_car:str, distance:int, fuel:int)-> dict:
    cars_collection[any_car]["Mileage"] += distance
    cars_collection[any_car]["Fuel"] -= fuel
    print(f"{any_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    if cars_collection[any_car]["Mileage"] >= 100000:
        del cars_collection[any_car]
        print(f"Time to sell the {any_car}!")
    return cars_collection

def revert(cars_collection:dict, any_car_for_revert:str, mileage_to_revert)-> dict:
    cars_collection[any_car_for_revert]["Mileage"] -= mileage_to_revert
    if cars_collection[any_car_for_revert]["Mileage"] < 10000:
        cars_collection[any_car_for_revert]["Mileage"] = 10000
    else:
        print(f"{any_car_for_revert} mileage decreased by {mileage_to_revert} kilometers")
    return cars_collection

def main():

    number_of_cars = int(input())

    collection_of_cars = {}

    for _ in range(number_of_cars):
        car, mileage,fuel = input().split("|")
        if car not in collection_of_cars:
            collection_of_cars[car] = {"Mileage": int(mileage), "Fuel": int(fuel)}

    command = input()

    while True:

        if command == "Stop":
            break

        action = command.split(" : ")

        if action[0] == "Drive":
            current_car, distance_to_go, fuel_needed = action[1], int(action[2]), int(action[3])
            if fuel_needed > collection_of_cars[current_car]["Fuel"]:
                print("Not enough fuel to make that ride")
            else:
                collection_of_cars = drive(collection_of_cars, current_car, distance_to_go, fuel_needed)

        elif action[0] == "Refuel":
            car_needed_refuel, fuel_for_refilling = action[1], int(action[2])
            filled_amount = fuel_for_refilling
            collection_of_cars[car_needed_refuel]["Fuel"] += fuel_for_refilling
            if collection_of_cars[car_needed_refuel]["Fuel"] > 75:
                filled_amount = fuel_for_refilling - (collection_of_cars[car_needed_refuel]["Fuel"] - 75)
                collection_of_cars[car_needed_refuel]["Fuel"] = 75
            print(f"{car_needed_refuel} refueled with {filled_amount} liters")

        elif action[0] == "Revert":
            car_for_revert, mileage_revert = action[1], int(action[2])
            collection_of_cars = revert(collection_of_cars, car_for_revert, mileage_revert)

        command = input()

    for vehicle in collection_of_cars.keys():
        mileage_total = collection_of_cars[vehicle]["Mileage"]
        fuel_total = collection_of_cars[vehicle]["Fuel"]
        print(f"{vehicle} -> Mileage: {mileage_total} kms, Fuel in the tank: {fuel_total} lt.")

main()





