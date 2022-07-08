import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    pass

#### Tokenizing ####
# a = "How long does shipping take?"
# print(a)
# a = tokenize(a)
# print(a)

#### Stemming with lower casing ####
words = ["organize", "Organizes", "organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)