number_of_rooms = int(input())
free_chairs = 0
not_enough = False

for room in range(1,number_of_rooms + 1):
    chairs, visitors = input().split()


    if len(chairs) > int(visitors):
        free_chairs += len(chairs) - int(visitors)

    elif len(chairs) < int(visitors):
        not_enough_chairs = int(visitors) - len(chairs)
        print(f"{not_enough_chairs} more chairs needed in room {room}")
        not_enough = True

if not not_enough:
    print(f"Game On, {free_chairs} free chairs left")


