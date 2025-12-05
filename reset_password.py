def main():
    initial_string = input()

    command = input()

    while command != "Done":

        command = command.split(" ")
        action = command[0]

        if action == "TakeOdd":
            new_raw_password = ''
            for index in range(len(initial_string)):
                if index % 2 != 0:
                    new_raw_password += initial_string[index]
            initial_string = new_raw_password
            print(initial_string)

        elif action == "Cut":
            cut_index, length = int(command[1]), int(command[2])
            cut_end_index = cut_index + length
            initial_string = initial_string[:cut_index] + initial_string[cut_end_index:]
            print(initial_string)

        elif action == "Substitute":
            substring, replacement = command[1], command[2]
            if substring in initial_string:
                initial_string = initial_string.replace(substring, replacement)
                print(initial_string)
            else:
                print("Nothing to replace!")

        command = input()

    print(f"Your password is: {initial_string}")

main()