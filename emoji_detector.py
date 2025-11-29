import re

initial_text = input()

treasure = []
treasure_coolness = 1

pattern = r"(\*\*|::)([A-Z][a-z]{2,})(\1)"

matches = re.findall(pattern, initial_text)

for index in initial_text:
    if index.isdigit():
        treasure_coolness *= int(index)

for match in matches:
    treasure.append(match[1])

for emoji in treasure:
    cool_treasure_sum = 0
    for char in emoji:
        cool_treasure_sum += ord(char)
    if cool_treasure_sum < treasure_coolness:
        treasure.remove(emoji)


print(f"Cool threshold: {treasure_coolness}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")
for item in matches:
    if item[1] in treasure:
        print(f"{''.join(item)}")


