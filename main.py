def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    single_words = text.split()
    words_number = word_count(single_words)
   
    lower_case_text = text.lower()
    count_characters = chara_count(lower_case_text)
    wb = make_list_dict(count_characters)
    wb.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---\n {words_number} words found in the document \n {report(wb)}\n --- End report ---")
    
def chara_count(book):
    letters_only = ''.join([x for x in book if x.isalpha()])
    characters = []
    characters[:] = letters_only
    
    dict_characters = {}
    for chara in characters: 
        if chara in dict_characters:
            dict_characters[chara] += 1
        else:
            dict_characters[chara] = 1
    
    
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
    


def make_list_dict(woerterbuch):
    return [{"letter": x, "Num": woerterbuch[x]} for x in woerterbuch]
    
def sort_on(dict):
    return dict["Num"]

def report(data):
    bookreport = ""
    for entry in data:
        bookreport += f"\n The '{entry['letter']}' character was found {entry['Num']} times"
    return bookreport

main()

