import re

text = input()

all_calories = 0


pattern = r'([|]|#)([A-z\s]+)\1(\d+\/\d+\/\d+)\1(\d+)\1'

matches = re.findall(pattern, text)

days_last = 0

for match in matches:
    item, best_before, calories = match[1], match[2], int(match[3])
    all_calories += calories

days_last = all_calories // 2000
print(f"You have food to last you for: {days_last} days!")

for index in matches:
    item = index[1]
    expire_date = index[2]
    nutrition = index[3]
    print(f"Item: {item}, Best before: {expire_date}, Nutrition: {nutrition}")

