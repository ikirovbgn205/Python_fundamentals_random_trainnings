def main():

    number_of_pieces = int(input())

    dictionary_of_pieces = {}

    for _ in range(number_of_pieces):
        entering_piece, entering_composer, entering_key = input().split("|")

        if entering_piece not in dictionary_of_pieces:
            dictionary_of_pieces[entering_piece] = {
                "composer": entering_composer,
                "key": entering_key
            }


    command = input()

    while command != "Stop":

        command = command.split("|")
        action = command[0]

        if action == "Add":
            piece, composer, key = command[1], command[2], command[3]
            if piece in dictionary_of_pieces:
                print(f"{piece} is already in the collection!")
            else:
                dictionary_of_pieces[piece] = {
                    "composer": composer,
                    "key": key
                }
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif action == "Remove":
            removing_piece = command[1]
            if removing_piece in dictionary_of_pieces:
                del dictionary_of_pieces[removing_piece]
                print(f"Successfully removed {removing_piece}!")
            else:
                print(f"Invalid operation! {removing_piece} does not exist in the collection.")

        elif action == "ChangeKey":
            current_piece, new_key = command[1], command[2]
            if current_piece in dictionary_of_pieces:
                dictionary_of_pieces[current_piece]["key"] = new_key
                print(f"Changed the key of {current_piece} to {new_key}!")
            else:
                print(f"Invalid operation! {current_piece} does not exist in the collection.")

        command = input()

    for printing_piece in dictionary_of_pieces.keys():
        printing_composer = dictionary_of_pieces[printing_piece]["composer"]
        printing_key = dictionary_of_pieces[printing_piece]["key"]
        print(f"{printing_piece} -> Composer: {printing_composer}, Key: {printing_key}")

main()