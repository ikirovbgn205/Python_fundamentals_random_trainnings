initial_energy = 100
initial_coins = 100

ongoing_events = input().split("|")

closed_factory = False

for event_objects in ongoing_events:
    event, amount = event_objects.split("-")

    if event == "rest":
        total_energy = initial_energy
        initial_energy += int(amount)
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - total_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event == "order":
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += int(amount)
            print(f'You earned {amount} coins.')
        else:
            initial_energy += 50
            print("You had to rest!")

    else:
        if initial_coins >= int(amount):
            initial_coins -= int(amount)
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            closed_factory = True
            break

if not closed_factory:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")


