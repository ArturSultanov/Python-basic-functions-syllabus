filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exits.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    