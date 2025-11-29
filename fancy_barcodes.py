import re

sequence_of_words = int(input())
list_of_matches = []

for _ in range(sequence_of_words):
    word = input()
    pattern = r"\B@#+\b([A-Z][A-Za-z0-9]+\b)\W#*\B"
    matches = re.findall(pattern, word)

    list_of_matches.append(matches)

for match in list_of_matches:
    if match:
        current_match = match[0]
        current_num = ""
        for char in current_match:
            if char.isdigit():
                current_num += char
        if not current_num:
            current_num = "00"
        print(f"Product group: {current_num}")
    else:
        print("Invalid barcode")