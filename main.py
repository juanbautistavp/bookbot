def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_characters = sort_char_count(char_count)
    
    print_report(book_path, word_count, sorted_characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    sorted_char_count = [{'char': k, 'count': v} for k, v in char_count.items()]
    sorted_char_count.sort(key=lambda x: x['count'], reverse=True)
    return sorted_char_count

def print_report(book_path, word_count, sorted_characters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for entry in sorted_characters:
        char = entry['char']
        count = entry['count']
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()