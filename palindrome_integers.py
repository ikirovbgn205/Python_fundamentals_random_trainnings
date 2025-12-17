def palindrome_checker(numbers:list)-> list:
    results = []

    for num in numbers:
        reversed_num = num[::-1]
        if reversed_num == num:
            results.append("True")
        else:
            results.append("False")

    return results

def main():
    positive_numbers = [num for num in input().split(", ")]

    is_palindrome = palindrome_checker(positive_numbers)
    print("\n".join(is_palindrome))

main()