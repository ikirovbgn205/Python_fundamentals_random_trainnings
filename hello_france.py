marketplace = input().split("|")

current_budget = int(input())

bought_items_price = []
sold_items_price_list = []
total_price_sold_items = 0

for purchase in marketplace:
    item, price = purchase.split("->")

    if item == "Clothes" and float(price) <= 50:
        if current_budget >= float(price):
            current_budget -= float(price)
            bought_items_price.append(float(price))

    elif item == "Shoes" and float(price) <= 35:
        if current_budget >= float(price):
            current_budget -= float(price)
            bought_items_price.append(float(price))


    elif item == "Accessories" and float(price) <= 20.50:
        if current_budget >= float(price):
            current_budget -= float(price)
            bought_items_price.append(float(price))

for new_price in bought_items_price:
    current_budget += new_price + (new_price * 0.40)
    sold_price = new_price + (new_price * 0.40)
    total_price_sold_items += sold_price
    sold_items_price_list.append(f"{sold_price:.2f}")

profit = total_price_sold_items - sum(bought_items_price)

print(" ".join(map(str, sold_items_price_list)))
print(f"Profit: {profit:.2f}")

if current_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")