file_path = '/Users/artursultanov/Python-projects/python-repeating-basics/files-and-exeptions/text-files/pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{len(pi_string)}: {pi_string}")
