from stats import get_word_count, get_character_amount, get_sorted_dict
#Reads text file and returns contents
def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
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
