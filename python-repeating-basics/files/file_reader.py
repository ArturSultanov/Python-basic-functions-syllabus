file_path = '/Users/artursultanov/Python-projects/python-repeating-basics/files-and-exeptions/text-files/pi_digits.txt'

with open(file_path) as file_object:
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())  
       