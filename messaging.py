sequence_of_numbers = input().split()

sequence_of_words = input()
message = ""

for number in sequence_of_numbers:
    index = 0

    for num in number:
        index += int(num)

    while index >= len(sequence_of_words):
        index -= len(sequence_of_words)


    message += sequence_of_words[index]
    sequence_of_words = sequence_of_words.replace(sequence_of_words[index], "", 1)

print(message)