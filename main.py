def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    return book_contents

def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def main(): 
    word_count = get_word_count(get_book_text())
    print(f"{word_count} words found in the document")

main()
