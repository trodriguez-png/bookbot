def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictionary = word_appearance(text)
    list = sort_on(dictionary)
    print("============ BOOTBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print("------------ Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count ---------")
    for item in list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("=============== END ==============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
from stats import get_num_words, word_appearance, sort_on

main()