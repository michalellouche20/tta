def generate_multiples(number, length):
    multiples_list = [number * i for i in range(1, length + 1)]
    return multiples_list

user_number = int(input("Enter a number: "))
user_length = int(input("Enter the length: "))

result_list = generate_multiples(user_number, user_length)
print(result_list)

#Challenge 2:
def remove_duplicate_consecutive_letters(word):
    cleaned_word = ''
    for i in range(len(word)):
        if i == 0 or word[i] != word[i - 1]:
            cleaned_word += word[i]
    return cleaned_word

user_word = input("Enter a word: ")

result_word = remove_duplicate_consecutive_letters(user_word)
print(result_word)