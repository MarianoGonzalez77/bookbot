def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string

def word_count(filepath):
    num_words = 0
    text = get_book_text(filepath)
    words = text.split()
    num_words = len(words)
    return num_words

character = {}
def char_count(filepath):
    text = get_book_text(filepath)
    text = text.lower()
    for char in text:
        if char in character:
            character[char] += 1
        else:
            character[char] = 1
    return character

char_list = []
def sort_start(dict_to_sort):
    for char, count in dict_to_sort.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_on(dict_item):
    return dict_item["count"]

def sort_count(dict_to_count):
    dict_to_count.sort(reverse=True, key=sort_on)
    return char_list
