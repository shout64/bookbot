
book = input("What is the path of the book you want to analyze?\n")

def main():
    with open(book) as f:
        file_contents = f.read()

    print("\n--- Begin report ---\n")
    print(f"Word count: {count_words(file_contents)}\n")
    count_characters(file_contents)
    print("\n--- End report ---")

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
        if i.isalpha():
            print("The '", i, "' character was found , ", character_count[i], " times")

main()
