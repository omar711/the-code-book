import sys
from common import alphabet

def increment(dictionary, key):
    if key in dictionary:
        dictionary[key] = dictionary[key] + 1
    else:
        dictionary[key] = 1


def message_statistics(input):
    words = {}
    characters = {}

    for line in input:
        line = line.lower()


        word_tokens = line.split()

        for word_token in word_tokens:
            increment(words, word_token)
        
        for character in line:
            if character in alphabet:
                increment(characters, character)

    return (words, characters) 


def print_in_order(dictionary, limit=len(alphabet)):
    ordered = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    ordered = ordered[:min(len(ordered), limit)]
    for key, value in ordered:
        print(value, "\t", key)


def short_words(dictionary, max_length=3):
    filtered = {}
    for key in dictionary:
        if len(key) <= max_length:
            filtered[key] = dictionary[key]
    
    return filtered


if __name__ == '__main__':
    
    if len(sys.argv) != 1:
        print("Usage: message_statistics.py")
        sys.exit(1)

    (words, characters) = message_statistics(sys.stdin)

    word_limit = 10
    short_word_limit = 5

    print("Top {} words:".format(word_limit))
    print_in_order(words, limit=10)

    print()
    print("Top {} short words".format(short_word_limit))
    print_in_order(short_words(words), limit=short_word_limit)

    print()
    print("Top characters:")
    print_in_order(characters)
