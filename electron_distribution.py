number_of_electrons = int(input())


filling = 0
filled_shells = []

while True:
    filling += 1
    shell = 2 * (filling ** 2)

    if number_of_electrons >= shell:
        number_of_electrons -= shell
        filled_shells.append(shell)

    else:
        if not number_of_electrons <= 0:
            filled_shells.append(number_of_electrons)
        break


print(filled_shells)
