responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n> ")
    response = input("Which mountain would you like to clim someday?\n> ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)\n> ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
