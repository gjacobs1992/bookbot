from stats import get_num_words, get_num_chars, sort_dict
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    get_num_words()
    print("----------- Character Count -----")
    char_dict = get_num_chars()
    sorted_list = sort_dict(char_dict)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
