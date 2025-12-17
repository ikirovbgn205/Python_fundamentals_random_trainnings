def smallest(first_num : int, second_num : int, third_number: int) -> int:
    list = [first_num, second_num, third_number]
    result = min(list)
    return result


def main():
    number_one = int(input())
    number_two = int(input())
    number_three = int(input())

    result = smallest(number_one, number_two, number_three)
    print(result)

main()