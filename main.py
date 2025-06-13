from stats import get_num_words
from stats import get_count_chars
from stats import sort_dict
import sys

def get_book_text(f_book) :
    try:
        with open(f_book) as f:
            print(f"Analyzing book found at {f_book}...")
            return f.read()
    except Exception as e: 
        print(e)
        print("============= END ===============")
        sys.exit(1)

def main() :
    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("============= END ===============")
        sys.exit(1)
    else :
        path_book = sys.argv[1]
    s_book = get_book_text(path_book)
    num_words = get_num_words(s_book)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    data = sort_dict(get_count_chars(s_book))
    for d in data :
        print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

main()
