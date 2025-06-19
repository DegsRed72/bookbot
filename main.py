from stats import get_word_count, get_character_amount, get_sorted_dict

def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    return book_contents

def main(): 
    text = get_book_text()
    word_count = get_word_count(text)
    char_dict = get_character_amount(text)
    #sorted_dict = get_sorted_dict(char_dict)
    print(f"{word_count} words found in the document")
    print(char_dict)

main()
