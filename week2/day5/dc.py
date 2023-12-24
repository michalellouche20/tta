input_sequence = input("Enter a comma-separated sequence of words: ")

words = [word.strip() for word in input_sequence.split(',')]

sorted_words = sorted(words)

output_sequence = ','.join(sorted_words)
print("Sorted Words:", output_sequence)

#Challenge 2: Longest Word

def longest_word(sentence):
    words = [word.strip(".,'") for word in sentence.split()]

    longest = max(words, key=len)

    return longest

print(longest_word("Margaret's toy is a pretty doll.")) 
print(longest_word("A thing of beauty is a joy forever.")) 
print(longest_word("Forgetfulness is by all means powerless!")) 