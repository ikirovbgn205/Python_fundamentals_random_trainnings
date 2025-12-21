wagons = int(input())

train = []

for wagon in range(wagons):
    train.append(int(wagon * 0))

command = input()

while command != "End":

    action = command.split()

    if action[0] == "add":
        train[-1] += int(action[1])

    elif action[0] == "insert":
        index = int(action[1])
        train[index] += int(action[2])

    elif action[0] == "leave":
        index = int(action[1])
        train[index] -= int(action[2])

    command = input()

print(train)

