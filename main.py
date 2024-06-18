def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    single_words = text.split()
    words_number = word_count(single_words)
    print(words_number)
    lower_case_text = text.lower()
    count_characters = chara_count(text)
    print(count_characters)
    
def chara_count(book):
    characters = []
    characters[:] = book
    dict_characters = {}
    for character in characters: 
        if character in dict_characters:
            dict_characters[character] += 1
        else:
            dict_characters[character] = 1
    return dict_characters
    

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

