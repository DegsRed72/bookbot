def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def get_character_amount(text):
    lowercase_text = text.lower()
    character_dictionary = {}
    for char in lowercase_text:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def get_sorted_dict(char_dict):
    char_dict.sort(key=sort_on, reverse=True)
    return char_dict
   
