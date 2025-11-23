def receive(some_dictionary: dict, some_task: list) -> dict:
    quantity, type_food = int(some_task[1]), some_task[2]
    if type_food not in some_dictionary.keys():
        some_dictionary[type_food] = 0
    if quantity > 0:
        some_dictionary[type_food] += quantity
    return some_dictionary

def sell(some_dictionary: dict, some_task: list,) -> dict:
    quantity, type_food = int(some_task[1]), some_task[2]
    if type_food not in some_dictionary.keys():
        print(f"You do not have any {type_food}.")
    elif some_dictionary[type_food] < quantity:
        sold_out = some_dictionary[type_food]
        del some_dictionary[type_food]
        print(f"There aren't enough {type_food}. You sold the last {sold_out} of them.")
    else:
        some_dictionary[type_food] -= quantity
        print(f"You sold {quantity} {type_food}.")
        if some_dictionary[type_food] <= 0:
            del some_dictionary[type_food]
        return some_dictionary
    return some_dictionary


def main():
    command = input()
    stoke_dictionary = {}
    total_receive_goods = 0
    total_left_goods = 0

    while True:

        if command == "Complete":
            break

        task = command.split(" ")

        if task[0] == "Receive":
            quantity = int(task[1])
            total_receive_goods += quantity
            stoke_dictionary = receive(stoke_dictionary, task)

        elif task[0] == "Sell":
            stoke_dictionary = sell(stoke_dictionary, task)

        command = input()

    for key, value in stoke_dictionary.items():
        print(f"{key}: {value}")

    for value in stoke_dictionary.values():
        total_left_goods += value
    all_sold_goods = total_receive_goods - total_left_goods
    print(f"All sold: {all_sold_goods} goods")

main()