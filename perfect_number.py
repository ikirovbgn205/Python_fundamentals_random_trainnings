def number_checker(num: int) -> str:
    divisors_sum = 0
    for number in range(1, num):
        if num % number == 0:
            divisors_sum += number

    if divisors_sum == num:
        return "We have a perfect number!"

    else:
        return "It's not so perfect."

def main():
    the_number = int(input())

    result = number_checker(the_number)
    print(result)

main()