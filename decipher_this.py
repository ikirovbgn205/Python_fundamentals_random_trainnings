cipher = input().split()

final_string = []
current_word = ""

for word in cipher:
    number = "".join([num for num in word if num.isdigit()])
    chars = "".join([char for char in word if not char.isdigit()])
    if len(chars) > 1:
        new_chars_composition = chars[-1] + chars[1:-1] + chars[0]
        new_word = chr(int(number)) + new_chars_composition
        final_string.append(new_word)
    else:
        new_word = chr(int(number)) + chars[0]
        final_string.append(new_word)

print(" ".join(final_string))