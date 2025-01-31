
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(f"Word count: {count_words(file_contents)}")
    print(f"Character count: \n{count_characters(file_contents)}")

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_characters(text):
    book = text.lower()
    character_count = {}
    for char in book:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char]  = 1
    
    for i in character_count:
        print("The '", i, "' character was found , ", i, " times")

main()
