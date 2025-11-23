def contains(some_key: str, some_sub: str) -> None:
    if some_sub in some_key:
        print(f"{some_key} contains {some_sub}")
    else:
        print(f"Substring not found!")


def flip(some_key: str, up_or_low: str, first_index: int, last_index: int) -> str:
    before_flip = some_key[:first_index]
    after_flip = some_key[last_index:]
    flipped = some_key[first_index:last_index]
    if up_or_low == "Upper":
        flipped = flipped.upper()
    elif up_or_low == "Lower":
        flipped = flipped.lower()
    final_key = before_flip + flipped + after_flip
    print(final_key)
    return final_key

def sliceing(some_key: str, first_index: int, last_index: int) -> str:
    before_slice = some_key[:first_index]
    after_slice = some_key[last_index:]
    sliced = before_slice + after_slice
    print(sliced)
    return sliced

raw_activation_keys = input()

while True:

    command = input()

    if command == "Generate":
        break

    command = command.split(">>>")

    action = command[0]

    if action == "Contains":
        sub_string = command[1]
        contains(raw_activation_keys, sub_string)

    elif action == "Flip":
        upper_or_lower = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        raw_activation_keys = flip(raw_activation_keys, upper_or_lower, start_index, end_index)

    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_keys = sliceing(raw_activation_keys, start_index, end_index)


print(f"Your activation key is: {raw_activation_keys}")