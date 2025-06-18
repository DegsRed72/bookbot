def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count
def get_character_amount(text):
    lowercase_text = text.lower()
    character_list = {}
    for char in lowercase_text:
        if char in character_list:
            character_list[char] += 1
        else:
            character_list[char] = 1
    return character_list
