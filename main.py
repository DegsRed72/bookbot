from stats import get_word_count, get_character_amount, get_sorted_dict
import sys

#Reads text file and returns contents as str
def get_book_text():
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as book:
            book_contents = book.read()
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return book_contents

def main(): 
    text = get_book_text()
    word_count = get_word_count(text)
    char_dict = get_character_amount(text)
    sorted_dict = get_sorted_dict(char_dict)
    print(f"Found {word_count} total words")
    for c in sorted_dict:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["value"]}")

main()
