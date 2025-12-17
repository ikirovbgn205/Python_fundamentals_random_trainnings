numbers = [int(num) for num in input().split()]

result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))