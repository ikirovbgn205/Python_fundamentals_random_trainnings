import re

text_string = input()

word_pairs = []

pattern = r"([@#])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.findall(pattern, text_string)


for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word[::-1] == second_word:
        word_pairs.append(f"{first_word} <=> {second_word}")
if not matches:
    print("No word pairs found!")

else:
    print(f"{len(matches)} word pairs found!")

if not word_pairs:
    print("No mirror words!")

else:
    print("The mirror words are:")
    print(", ".join(word_pairs))


