file_path = '/Users/artursultanov/Python-projects/python-repeating-basics/files-and-exeptions/text-files/large_pi_digit.txt'

length_of_pi = input("Enter length of the pi you want to check.\n> ")

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines[:13000]:
    pi_string += line.strip()

pi_string_limited = pi_string[:int(length_of_pi)]

birthday = input("Enter your birthday, in the form mmddyy!\n> ")
if birthday in pi_string_limited:
    print("Your birthday appears in the first million digits of pi!")
else:
    print(f"Your birthday does not appear in the first {length_of_pi} digits of pi.")
