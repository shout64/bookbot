
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(f"Character count: {count_characters(file_contents)}")

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
    
    return character_count

main()
