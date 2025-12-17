def odd_even_sums(some_number:str )-> str:
    odd_sum = 0
    even_sum = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


def main():
    single_number = input()

    result = odd_even_sums(single_number)
    print(result)

main()
