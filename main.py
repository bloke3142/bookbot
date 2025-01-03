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

def dict_to_list(dictionary):
    #make empty list
    list = []
    #iterate dictionary and add to list
    for i in dictionary:
          list.append({"letter": i, "count": dictionary[i]})
    return list

def sort_on(dict):
    return dict["count"]



def char_count_descending(list):
     #sort list of dictionarys from high to low count
     list.sort(reverse=True, key=sort_on)
     return list

def print_list(list):
     for dict in list:
          print(f"Letter '{dict["letter"]}' appears {dict["count"]} times")

def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        #print(file_contents)
        words = count_words(file_contents)
        print(f"Report on {book} :-")
        print()
        print(f"Number of words: {words}")
        print()
        characters = count_characters(file_contents)
        #print(characters)
        list_of_chars = dict_to_list(characters)
        #print(list_of_chars)
        descending_list = char_count_descending(list_of_chars)
        #print(descending_list)
        print_list(descending_list)
        print()
        print("End of report")

main()