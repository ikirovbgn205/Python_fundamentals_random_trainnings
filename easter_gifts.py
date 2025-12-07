list_of_gifts = input().split()

command = input()

while command != "No Money":

    command = command.split()
    action = command[0]

    if action == "OutOfStock":
        gift = command[1]
        if gift in list_of_gifts:
            for index in range(len(list_of_gifts)):
                if list_of_gifts[index] == gift:
                    list_of_gifts[index] = "None"

    elif action == "Required":
        gift = command[1]
        index = int(command[2])
        if 0 < index < len(list_of_gifts):
            list_of_gifts[index] = gift

    elif action == "JustInCase":
        gift = command[1]
        list_of_gifts[-1] = gift

    command = input()

list_without_none = []
for my_gift in list_of_gifts:
    if not my_gift == "None":
        list_without_none.append(my_gift)

print(" ".join(list_without_none))
