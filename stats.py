def get_num_words(text):
    words = text.split()
    return len(words)

def word_appearance(text):
    letter_dictionary = {}
    lowered_text = text.lower() 
    for word in lowered_text:
        if word in letter_dictionary:
            letter_dictionary[word] += 1 
        else:
            letter_dictionary[word] = 1
    return letter_dictionary

def sort_on_helper(dict_item):
    return dict_item["num"]

def sort_on(dictionary):
    char_list = []
    for char, count in dictionary.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True, key =sort_on_helper)
    return char_list       