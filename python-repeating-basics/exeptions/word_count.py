def count_words(filename):
    """Counter of approximately number of words in the file"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exits.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
        
filenames = ['alice.txt', 'sidhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
    