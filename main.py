def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
    return book_contents
def main():
    all_words = get_book_text()
    print(all_words)
main()
