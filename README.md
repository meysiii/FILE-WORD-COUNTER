# 🔤 Word Counter (Python)

AUTHOR : M.S.MEYSINTHA

A simple Python project that counts the number of words, characters, and lines in a given text or file.
This project is useful for beginners to understand file handling, string manipulation, and basic text processing in Python.

# 📌 Features

✅ Count words in a text/file
✅ Count characters (with/without spaces)
✅ Count lines in a file
✅ Works with user input or external text files
✅ Beginner-friendly and easy to use

# 📜 Code Example
def word_counter(file_name):
    try:
        with open(file_name, "r") as file:
            text = file.read()
            
            # Counts
            words = len(text.split())
            characters = len(text)
            lines = len(text.splitlines())
            
            print("📑 File Analysis:")
            print(f"➡️ Total Words: {words}")
            print(f"➡️ Total Characters: {characters}")
            print(f"➡️ Total Lines: {lines}")
    except FileNotFoundError:
        print("❌ File not found. Please check the filename.")


# Example Usage
file_name = input("Enter file name: ")
word_counter(file_name)

# ▶️ Example Run
Enter file name: sample.txt

# 📑 File Analysis:
➡️ Total Words: 120
➡️ Total Characters: 750
➡️ Total Lines: 15

# ⚡ How to Run

Clone this repository:

git clone https://github.com/your-username/word-counter.git
cd word-counter


Place your text file in the project folder (example: sample.txt)

# Run the program:

python word_counter.py

# Output



# 🚀 Future Improvements

Add option to exclude punctuation marks

Display top frequent words (word frequency analysis)

Add GUI version using Tkinter

Extend to count paragraphs and sentences

Add support for PDF/Docx files
