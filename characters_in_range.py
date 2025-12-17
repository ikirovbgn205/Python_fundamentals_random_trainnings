def between(char_one:str, char_two:str)->list:

    between_list = []

    for symbol in range(ord(char_one) + 1, ord(char_two)):
        between_list.append(chr(symbol))

    return between_list

def main ():
    first_char = input()
    second_char = input()

    result = between(first_char, second_char)

    print(" ".join(result))

main()