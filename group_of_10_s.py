cluster_of_numbers = [int(num) for num in input().split(", ")]

group = 10


while cluster_of_numbers:
    group_list = [number for number in cluster_of_numbers if number <= group]
    cluster_of_numbers = [number for number in cluster_of_numbers if number not in group_list]
    print(f"Group of {group}'s: {group_list}")
    group += 10
    group_list = []