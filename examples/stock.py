delivery = input().split()

stokes = {}

for i in range(0, len(delivery), 2):
    stoke = delivery[i]
    quantity = int(delivery[i + 1])
    stokes[stoke] = quantity

checking = input().split()

for word in checking:
    if word not in stokes.keys():
        print(f"Sorry, we don't have {stoke}")
    else:
        for stoke, quantity in stokes.items():
            print(f'We have {quantity} of {stoke} left')
