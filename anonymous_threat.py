initial_string = input().split()

command = input()

while command != "3:1":

    command = command.split()
    action = command[0]

    if action == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index not in range(len(initial_string)):
            start_index = 0
        if end_index not in range(len(initial_string)):
            end_index = len(initial_string) - 1
        merged_string = "".join(initial_string[start_index:end_index+1])
        initial_string[start_index] = "".join(initial_string[start_index: end_index + 1])
        initial_string = initial_string[:start_index + 1] + initial_string[end_index + 1:]

    elif action == "divide":
        index = int(command[1])
        partition = int(command[2])
        element = initial_string[index]
        partition_size = len(element) // partition
        count_of_partitions = 0
        partitioned_list = []
        for current_index in range(0, len(element), partition_size):
            count_of_partitions += 1
            if count_of_partitions == partition:
                current_partition = element[current_index:]
                partitioned_list.append(current_partition)
                break
            else:
                current_partition = element[current_index:current_index + partition_size]
                partitioned_list.append(current_partition)
        initial_string = initial_string[:index] + partitioned_list + initial_string[index + 1:]

    command = input()

print(" ".join(initial_string))