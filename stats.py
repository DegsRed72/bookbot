# Returns word count of the text
def get_word_count(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

# Returns a dictionary of each character and the amount of times it appears in the text
def get_character_amount(text):
    lowercase_text = text.lower()
    character_dictionary = {}
    for char in lowercase_text:
        if char in character_dictionary:
            character_dictionary[char] += 1
        else:
            character_dictionary[char] = 1
    return character_dictionary

def sort_on(dict):
    return dict["value"]

# Returns a sorted list of dictionaries 
def get_sorted_dict(char_dict):
    sorted_dicts = []
    for char in char_dict:
        value = char_dict[char]
        sorted_dicts.append({"char": char, "value": value})
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
   
