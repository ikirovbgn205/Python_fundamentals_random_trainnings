initial_string = list(map(int, input().split(", ")))

list_of_indices = [i for i in range(len(initial_string)) if initial_string[i] % 2 == 0]
print(list_of_indices)

