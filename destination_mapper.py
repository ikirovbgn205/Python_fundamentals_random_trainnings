import re

unscraped_text = input()

pattern = r"(=|\/)([A-Z][a-zA-z]{2,})\1"

matches = re.findall(pattern, unscraped_text)

destinations = [location[1] for location in matches ]

travel_points = 0
for destination in destinations:
    travel_points += len(destination)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")