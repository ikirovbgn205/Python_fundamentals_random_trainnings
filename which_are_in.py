substrings = input().split(", ")
words = input().split(", ")

list_of_exsisting_substrings = []

for sub in substrings:
    for word in words:
        if sub in word:
            list_of_exsisting_substrings.append(sub)
            break

print(list_of_exsisting_substrings)