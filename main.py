def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    single_words = text.split()
    words_number = word_count(single_words)
    print(words_number)
    

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(book):
    words_total = 0
    for i in range(0, len(book)):
        words_total += 1
    return words_total
    



main()

