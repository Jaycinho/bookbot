import sys
from stats import get_num_words
from stats import get_num_letters
from stats import result

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

get_num_words(filepath)
letter_counter = get_num_letters(filepath)
result(letter_counter)