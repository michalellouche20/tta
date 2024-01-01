class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.split()
        return words.count(word)

    def most_common_word(self):
        words = self.text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        most_common_word = max(word_counts, key=word_counts.get)
        return most_common_word

    def unique_words(self):
        words = self.text.split()
        unique_words = []
        for word in words:
            if word not in unique_words:
                unique_words.append(word)
        return unique_words

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'stranger.txt') as file:
            text = file.read()
        return cls(text)

class TextModification(Text):
    def remove_punctuation(self):
        punctuation_chars = set(".,;:'\"!?()[]{}")
        cleaned_text = ''.join(char for char in self.text if char not in punctuation_chars)
        return cleaned_text

    def remove_stopwords(self):
        stop_words = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn"])
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        cleaned_text = ''.join(char for char in self.text if char.isalnum() or char.isspace())
        return cleaned_text

simple_text = "A good book would sometimes cost as much as a good house."
text_instance = Text(simple_text)
print(text_instance.word_frequency("good"))
print(text_instance.most_common_word())
print(text_instance.unique_words())

stranger_text_instance = Text.from_file('the_stranger.txt')
print(stranger_text_instance.word_frequency("meursault"))
print(stranger_text_instance.most_common_word())
print(stranger_text_instance.unique_words())

modified_text_instance = TextModification(simple_text)
print(modified_text_instance.remove_punctuation())
print(modified_text_instance.remove_stopwords())
print(modified_text_instance.remove_special_characters())