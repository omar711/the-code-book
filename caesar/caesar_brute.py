import sys
from common import alphabet 
from caesar import caesar_encrypt

common_words = set([
    "the", "and", "his", "her", "my", "your", "this", "those", "who", "why", "how"
])

def count_common_words(text):
    count = 0
    for token in text.split():
        if token in common_words:
            count = count + 1
    
    return count


if __name__ == '__main__':
    
    if len(sys.argv) != 1:
        print("Usage: caesar_brute.py")
        sys.exit(1)
    
    input = ""
    for line in sys.stdin:
        input = input + line.lower()

    most_likely_text = None
    most_likely_shift = None
    most_likely_count = 0

    for shift in range(len(alphabet)):
        decrypted = caesar_encrypt(input, -shift)
        print("Decrypted, shift = {}\n{}\n".format(shift, decrypted))

        common_count = count_common_words(decrypted)
        if common_count > most_likely_count:
            most_likely_count = common_count
            most_likely_shift = shift
            most_likely_text = decrypted

    print("The most likely shift is {} due to finding {} common words in its decrypted text\n{}".format(most_likely_shift, most_likely_count, most_likely_text))

