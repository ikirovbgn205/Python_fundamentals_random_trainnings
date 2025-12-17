def add(some_schedule : list, some_command : list ) -> list:
    some_lesson_title = some_command[1]
    if some_lesson_title not in some_schedule:
        some_schedule.append(some_lesson_title)
    return some_schedule

def swap(some_schedule : list, some_command : list ) -> list:
    first_lesson_for_swap = some_command[1]
    second_lesson_for_swap = some_command[2]
    first_exercise_for_swap = f"{first_lesson_for_swap}-Exercise"
    second_exercise_for_swap = f"{second_lesson_for_swap}-Exercise"
    if first_lesson_for_swap in some_schedule and second_lesson_for_swap in some_schedule:
        first_lesson_index = some_schedule.index(first_lesson_for_swap)
        second_lesson_index = some_schedule.index(second_lesson_for_swap)
        some_schedule[first_lesson_index], some_schedule[second_lesson_index] = \
            (some_schedule[second_lesson_index], some_schedule[first_lesson_index])

    if first_exercise_for_swap in some_schedule:
        current_index = some_schedule.index(second_lesson_for_swap) + 1
        some_schedule.pop(current_index)
        index_for_insertion = some_schedule.index(first_exercise_for_swap) + 1
        some_schedule.insert(index_for_insertion, first_exercise_for_swap)

    if second_exercise_for_swap in some_schedule:
        current_index = some_schedule.index(first_lesson_for_swap) + 1
        some_schedule.pop(current_index)
        index_for_insertion = some_schedule.index(second_lesson_for_swap) + 1
        some_schedule.insert(index_for_insertion, second_exercise_for_swap)

    return some_schedule

def exercise(some_schedule : list, some_command : list ) -> list:
    lesson_title_for_exercise = some_command[1]
    string_for_exercise = f"{lesson_title_for_exercise}-Exercise"
    if lesson_title_for_exercise in some_schedule:
        if string_for_exercise not in some_schedule:
            exercise_index = some_schedule.index(lesson_title_for_exercise) + 1
            some_schedule.insert(exercise_index, string_for_exercise)
    if lesson_title_for_exercise not in some_schedule:
        some_schedule.append(lesson_title_for_exercise)
        some_schedule.append(string_for_exercise)
    return some_schedule

initial_schedule = input().split(", ")

command = input()

while command != "course start":

    command = command.split(":")

    action = command[0]

    if action == "Add":
        initial_schedule = add(initial_schedule, command)

    elif action == "Insert":
        lesson_title = command[1]
        index = int(command[2])
        if lesson_title not in initial_schedule:
            initial_schedule.insert(index, lesson_title)

    elif action == "Remove":
        lesson_title = command[1]
        exercise_title = f"{lesson_title}-Exercise"
        if lesson_title in initial_schedule:
            initial_schedule.remove(lesson_title)

        if exercise_title in initial_schedule:
            initial_schedule.remove(exercise_title)

    elif action == "Swap":
        initial_schedule = swap(initial_schedule, command)

    elif action == "Exercise":
        initial_schedule = exercise(initial_schedule, command)

    command = input()

for index, item in enumerate(initial_schedule, start=1):
    print(f"{index}.{item}")

