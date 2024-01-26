import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


nltk.download('omw-1.4')

def get_synonyms_antonyms(word):
    synonyms = []
    antonyms = []

    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())

    return list(set(synonyms)), list(set(antonyms))

def get_synonyms_antonyms_from_phrase(phrase):
    tokens = word_tokenize(phrase)
    pos_tags = pos_tag(tokens)

    synonyms = {}
    antonyms = {}

    for token, pos in pos_tags:
        if pos.startswith('NN') or pos.startswith('VB') or pos.startswith('JJ') or pos.startswith('RB'):
            synonyms[token], antonyms[token] = get_synonyms_antonyms(token)

    return synonyms, antonyms

while True:
    # Get user input
    user_input = input("Enter a word or phrase (type 'exit' to end): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break

    # Example for a single word:
    synonyms, antonyms = get_synonyms_antonyms(user_input)
    print(f"Synonyms of '{user_input}': {synonyms}")
    print(f"Antonyms of '{user_input}': {antonyms}")

    # Example for a phrase:
    synonyms, antonyms = get_synonyms_antonyms_from_phrase(user_input)
    print(f"Synonyms of words in '{user_input}': {synonyms}")
    print(f"Antonyms of words in '{user_input}': {antonyms}")
