sequence_of_words = input().split()

current_word = input()

palindrome_list = [word for word in sequence_of_words if word == word[::-1]]
count_of_the_word = palindrome_list.count(current_word)

print(palindrome_list)
print(f"Found palindrome {count_of_the_word} times")