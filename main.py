def count_words(string):
        word_list = string.split()
        word_count = len(word_list)
        return word_count

def count_characters(string):
     #make empty dictionary
    character_count = {}

     #convert to lower case
    string = string.lower()
     
    abc = "abcdefghijklmnopqrstuvwxyz"
     #loop alphabet
    for i in range(len(abc)):
        #count number of each letter and add to dictionary
        character_count[abc[i]] = string.count(abc[i])
    #return dictionary of letter/number pairs
    return character_count

def char_count_descending(letters_count):
     #sort dictionary from high to low count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = count_words(file_contents)
        print(f"Number of words: {words}")
        characters = count_characters(file_contents)
        descending_list = char_count_descending(characters)
        #print letters and count in descending order

main()