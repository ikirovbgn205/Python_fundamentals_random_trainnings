coins_to_take_home = input().split(", ")
number_of_beggars = int(input())
coins_integer = []

for coin in coins_to_take_home:
    coins_integer.append(int(coin))

collected_coins = []
start_index = 0

for beggar in range(number_of_beggars):
    collection = 0
    for collect in range(start_index, len(coins_integer), number_of_beggars):
        collection += coins_integer[collect]
    collected_coins.append(collection)
    start_index += 1

print(collected_coins)