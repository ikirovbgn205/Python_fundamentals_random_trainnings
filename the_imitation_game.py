def move(some_message:str, number_of_moves:int) -> str:
    substring_to_be_moved = some_message[:number_of_moves]
    some_message = some_message[number_of_moves:] + substring_to_be_moved
    return some_message

def inserting(some_message:str, some_index:int, some_value:str) -> str:
    before_insert = some_message[:some_index]
    after_insert = some_message[some_index:]
    some_message = before_insert + some_value + after_insert
    return some_message

def change_all(some_message:str, any_substring:str, some_replacement_item:str) -> str:
    result = some_message.replace(any_substring, some_replacement_item)
    return result

def main():
    encrypted_message = input()

    command = input()

    while command != "Decode":

        command = command.split("|")
        action = command[0]

        if action == "Move":
            number_of_letters = int(command[1])
            encrypted_message = move(encrypted_message, number_of_letters)

        elif action == "Insert":
            index, value = int(command[1]), command[2]
            encrypted_message = inserting(encrypted_message, index, value)

        elif action == "ChangeAll":
            substring_for_replace, replacement_item = command[1], command[2]
            encrypted_message = change_all(encrypted_message, substring_for_replace, replacement_item)

        command = input()

    print(f"The decrypted message is: {encrypted_message}")

main()