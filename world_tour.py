def add_stop(string:str, some_index:int, insert_string:str)-> str:
    before_index = string[:some_index]
    after_index = string[some_index:]
    new_string = before_index + insert_string + after_index
    return new_string

def remove_stop(string:str, some_first_index:int, some_end_index:int)-> str:
    replacement_item = ''
    substring_needed_replacement = string[some_first_index:some_end_index]
    final_string = string.replace(substring_needed_replacement, replacement_item)
    return final_string

def switch(string:str, some_old_string:str, some_new_string:str)-> str:
    switched_string = string.replace(some_old_string, some_new_string)
    return switched_string


def main():
    planned_countries = input()
    command = input()
    while True :

        if command == "Travel":
            break

        command = command.split(':')
        action = command[0]

        if action == "Add Stop":
            index = int(command[1])
            string = command[2]
            if 0 <= index <= len(planned_countries):
                planned_countries = add_stop(planned_countries, index, string)
            print(planned_countries)


        elif action == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2]) + 1
            if 0 <= start_index <= len(planned_countries) and 0 <= end_index <= len(planned_countries):
                planned_countries = remove_stop(planned_countries, start_index, end_index)
            print(planned_countries)

        elif action == "Switch":
            old_string = command[1]
            new_string = command[2]
            if old_string in planned_countries:
                planned_countries = switch(planned_countries,old_string, new_string)
            print(planned_countries)


        command = input()

    print(f'Ready for world tour! Planned stops: {planned_countries}')
main()