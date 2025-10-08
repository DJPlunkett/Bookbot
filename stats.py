# Functions for analyzing book stats

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def sort_on(item):
    return item["num"]

def printout(path):
    book = get_book_text(path)
    try: print(book)
    except: print("Error encountered")

def word_count(path):
    book = get_book_text(path)
    words = book.split()
    wordcount = len(words)
    return wordcount

def character_count(path):
    book = get_book_text(path)
    book = book.lower()
    chara = {}
    current_chara = "a"
    while chr(ord(current_chara) - 1) != "z":
        chara[current_chara] = book.count(current_chara)
        current_chara = chr(ord(current_chara) + 1)
    return chara

def sorted_cc(path):
    base_chara = character_count(path)
    sort_chara = []
    for i in base_chara:
        temp_chara = {"char": i, "num": base_chara[i]}
        sort_chara.append(temp_chara)
    sort_chara.sort(reverse=True, key=sort_on)
    return sort_chara
