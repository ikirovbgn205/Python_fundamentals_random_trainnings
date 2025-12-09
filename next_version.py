current_version = input().split(".")


number = int("".join(current_version))

number += 1

new_version = ".".join(str(number))

print(new_version)