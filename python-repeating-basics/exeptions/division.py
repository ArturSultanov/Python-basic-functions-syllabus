print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:\n> ")
    if first_number == 'q' or first_number == 'quit':
        break
    second_number = input("Second number:\n> ")
    if second_number == 'q' or second_number == 'quit':
        break

    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(f"The answer is: {answer}.")
