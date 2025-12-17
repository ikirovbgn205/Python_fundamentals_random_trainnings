
def add(first_number:int, second_number:int)-> int:
    addition = first_number + second_number
    return addition

def subtract(first_number:int, second_number:int)-> int:
    subtraction = second_number - first_number
    return subtraction

def add_and_subtract(first_number:int, second_number:int, third_number:int)-> int:
    addition = add(first_number, second_number)
    subtraction = subtract(third_number, addition)
    return subtraction

def main():
    first_num = int(input())
    second_num = int(input())
    third_num = int(input())


    result = add_and_subtract(first_num, second_num, third_num)
    print(result)

main()