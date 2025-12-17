def formating(command:str ,some_target: str)-> None:

    if command == "int":
        result = int(some_target) * 2
        print(result)

    elif command == "real":
        result = int(some_target) * 1.5
        print("{:.2f}".format(result))

    elif command == "string":
        result = f"${some_target}$"
        print(result)


def main():
    command_input = input()
    target = input()

    formating(command_input, target)


main()