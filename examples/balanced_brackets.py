number_of_lines = int(input())

brackets = ""
balanced = "BALANCED"


for _ in range(number_of_lines):
    command = input()
    if command == '(':
        brackets +=command
    elif command == ')':
        brackets +=command

for i in range(0, len(brackets), 2):
    if brackets[i:i + 2] != '()':
        balanced = "UNBALANCED"

print(balanced)

