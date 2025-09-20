def word_counter(filename):
    try:
        with open(filename, "r") as f:
            text = f.read()
        words = text.split()
        print(f"Total words in {filename}: {len(words)}")
    except FileNotFoundError:
        print("File not found!")

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Hello world. Python is amazing!")

word_counter("sample.txt")
