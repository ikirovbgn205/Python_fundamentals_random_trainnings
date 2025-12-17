def factorial_division(number_one: int, number_two: int) -> int:
    first_factorial = 1
    second_factorial = 1
    for num in range(1,number_one + 1):
        first_factorial *= num

    for num in range(1,number_two + 1):
        second_factorial *= num

    result = first_factorial // second_factorial
    return result

def main():
    first_number = int(input())
    second_number = int(input())

    final_result = factorial_division(first_number, second_number)
    print(f"{final_result:.2f}")
main()