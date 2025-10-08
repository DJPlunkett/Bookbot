# Bookbot

from stats import word_count
from stats import sorted_cc

import sys

def main():
    sys_check = sys.argv
    if len(sys_check) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============BOOKBOT============")
    print(f"Analyzing book found at {sys_check[1]}...")
    num_words = word_count(sys_check[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    sort_count = sorted_cc(sys_check[1])
    print("--------- Character Count -------")
    for i in range(len(sort_count)):
        print(f"{sort_count[i]["char"]}: {sort_count[i]["num"]}")
    print("============= END ===============")
# Activation point

main()
