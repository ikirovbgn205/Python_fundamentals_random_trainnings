def main():
    sequence_of_numbers = [int(num) for num in input().split()]

    max_num = max(sequence_of_numbers)
    min_num = min(sequence_of_numbers)
    sum_of_numbers = sum(sequence_of_numbers)

    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_of_numbers}")

main()

