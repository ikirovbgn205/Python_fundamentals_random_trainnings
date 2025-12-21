list_of_vowels = ['a', 'o', 'u', 'e', 'i', "A", "O", "U", "E", "I"]

word_without_vowels = [char for char in input() if char not in list_of_vowels]

print("".join(word_without_vowels))
