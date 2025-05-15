import sys
from stats import word_count
from stats import char_count
from stats import sort_count
from stats import sort_start

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
char_dict = char_count(filepath)
char_list = sort_start(char_dict)
end_sort = sort_count(char_list)

def main():
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count(filepath)} total words
--------- Character Count -------""") 

    for item in end_sort:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()
