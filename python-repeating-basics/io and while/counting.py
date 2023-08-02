message = ""
current_number = 0

active = True

while active:
    current_number += 1
    message = input(f"{current_number}. Enter 'quit' or 'break' to end the the program.\n> ")
    
    if message == 'quit':
        active = False
    elif message == 'skip':
        continue
    elif message == 'break':
        break
    else:
        print(message)
