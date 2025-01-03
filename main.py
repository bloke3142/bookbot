def count_words(string):
        word_list = string.split()
        word_count = len(word_list)
        return word_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = count_words(file_contents)
        print(f"Number of words: {words}")

main()