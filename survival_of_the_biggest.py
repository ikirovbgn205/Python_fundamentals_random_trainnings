list_in_string = input().split()
number_of_removed_integers = int(input())

list_of_integers = []

for digit in list_in_string:
    list_of_integers.append(int(digit))

for i in range(number_of_removed_integers):
    list_of_integers.remove(min(list_of_integers))

new_list_of_integers = []

for number in list_of_integers:
    new_list_of_integers.append(str(number))

print(", ".join(new_list_of_integers))