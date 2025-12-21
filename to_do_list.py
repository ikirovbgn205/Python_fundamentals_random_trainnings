to_do_list = []

things_to_do = input()

while things_to_do != "End":

    to_do_list.append(things_to_do)

    things_to_do = input()

to_do_list = sorted(to_do_list)
new_list_to_do = []

for to_do in to_do_list:
    to_do = to_do.split("-")
    new_list_to_do.append(to_do[1])

print(new_list_to_do)