# text_processing_tool/count_words.py

def count_words(text):
    words = text.split()
    return len(words)


# text_processing_tool/find_unique_words.py

def find_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return unique_words

# text_processing_tool/convert_to_uppercase.py

def convert_to_uppercase(text):
    return text.upper()

# text_processing_tool/__init__.py

from .count_words import count_words
from .find_unique_words import find_unique_words
from .convert_to_uppercase import convert_to_uppercase


# main.py

from text_processing_tool import count_words, find_unique_words, convert_to_uppercase

def main():
    text = input("Enter a text string: ")

    print("\nText Processing Options:")
    print("1. Count words")
    print("2. Find unique words")
    print("3. Convert to uppercase")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        print(f"Number of words: {count_words(text)}")
    elif choice == '2':
        unique_words = find_unique_words(text)
        print(f"Unique words: {', '.join(unique_words)}")
    elif choice == '3':
        print(f"Uppercase text: {convert_to_uppercase(text)}")
    else:
        print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


text_processing_tool/
│
├── __init__.py
├── count_words.py
├── find_unique_words.py
└── convert_to_uppercase.py
main.py

