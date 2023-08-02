file_path = '/Users/artursultanov/Python-projects/python-repeating-basics/files-and-exeptions/text-files/large_pi_digit.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

max_chars = 100
pi_string_limited = pi_string[:max_chars]
print(f"{len(pi_string)}: {pi_string_limited}")
