cluster_of_numbers = [int(num) for num in input().split(", ")]

positive_numbers = []
negative_numbers = []
even_numbers = []
odd_numbers = []

for number in cluster_of_numbers:
    if number % 2 == 0:
        even_numbers.append(str(number))
        if number >= 0:
            positive_numbers.append(str(number))
        else:
            negative_numbers.append(str(number))

    else:
        odd_numbers.append(str(number))
        if number >= 0:
            positive_numbers.append(str(number))
        else:
            negative_numbers.append(str(number))

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")