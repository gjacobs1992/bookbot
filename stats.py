import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words():
    book = get_book_text(sys.argv[1])
    list_of_strings = book.split()
    print(f"Found {len(list_of_strings)} total words")

def get_num_chars():
    book = get_book_text(sys.argv[1])
    chars = list(book.lower())
    char_dict = {}
    for char in chars:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_list = []
    for key in dict:
        temp_dict = {"char": key, "num": dict[key]}
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list