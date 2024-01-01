import random

def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words):
    sentence_words = random.sample(words, length)
    sentence = ' '.join(sentence_words)
    return sentence.lower()

def main():
    print("Random Sentence Generator")

    try:
        sentence_length = int(input("Enter the length of the sentence (between 2 and 20): "))
        if not 2 <= sentence_length <= 20:
            raise ValueError("Invalid input. Length should be between 2 and 20.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    words = get_words_from_file("word_list.txt")
    random_sentence = get_random_sentence(sentence_length, words)
    
    print("Generated Sentence:")
    print(random_sentence)

if __name__ == "__main__":
    main()



import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary_value = data['company']['employee']['payable']['salary']
print("Salary:", salary_value)

data['company']['employee']['birth_date'] = "1990-01-01"

with open("output.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)


print("JSON saved to output.json")
stranger_text = Text.from_file('path/to/your/file/the_stranger.txt')
