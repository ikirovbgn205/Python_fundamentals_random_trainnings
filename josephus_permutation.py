waiting_circle = input().split()

killed_one = int(input())

executed = []

index = 0

while waiting_circle:

    index += killed_one

    while index > len(waiting_circle):
        index -= len(waiting_circle)

    executed.append(waiting_circle.pop(index - 1))
    index -= 1

print(f'[{",".join(executed)}]')