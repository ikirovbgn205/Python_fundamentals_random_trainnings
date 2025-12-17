def formating(command:str)-> None:

    if command == "int":
        target = int(input())
        result = target * 2
        print(result)

    elif command == "real":
        target = float(input())
        result = target * 1.5
        print("{:.2f}".format(result))

    elif command == "string":
        target = input()
        result = f"${target}$"
        print(result)


def main():
    command_input = input()

    formating(command_input)
main()