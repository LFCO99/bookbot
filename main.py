import sys

from stats import get_char_count, get_num_words, sort_dic


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dic = get_char_count(text)
    list_od = sort_dic(char_dic)
    print("=" * 12, "BOOKBOT", "=" * 12)
    print(f"Analyzing book found at {path}")
    print("-" * 11, "Word Count", "-" * 10)
    print(f"Found {num_words} total words")
    print("-" * 9, "Character Count", "-" * 7)
    for i in list_od:
        char = i["char"]
        num = i["num"]
        if char.isalpha():
            print(f"{char}: {num}")
        pass
    print("=" * 15, "END", "=" * 15)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


main()
