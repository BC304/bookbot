def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    alphabet_dict = get_alpha_chars_dict(text)
    char_sorted = dict(sorted(alphabet_dict.items(), reverse=True, key=lambda item: item[1]))
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for i in char_sorted:
        print(f"The '{i}' character was found {char_sorted[i]} times")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    lowered_words = text.lower()
    chars = {}
    for c in set(lowered_words):
       chars[c] = lowered_words.count(c)
    return chars

def get_alpha_chars_dict(text):
    lowered_words = text.lower()
    chars = {}
    for c in set(lowered_words):
        if c.isalpha():
            chars[c] = lowered_words.count(c)
    return chars

main()