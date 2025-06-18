from stats import get_word_count
from stats import get_character_amount

def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    return book_contents

def main(): 
    word_count = get_word_count(get_book_text())
    print(f"{word_count} words found in the document")
    print(get_character_amount(get_book_text()))

main()
