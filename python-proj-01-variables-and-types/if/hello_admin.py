user_names = ['admin', 'Eric', 'Nana',
              'Tom', 'Honza', 'ArTur',
              'Ayano', 'Pedro', 'George']

logginig_users = ['admin', 'Artur', 'SaM']

# user_names = []

current_users = []

if logginig_users:

    for name in user_names:
        current_users.append(name.lower())

    for name in logginig_users:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?")
        elif name.lower() not in current_users:
            print(f"Sorry {name}, you have to sign up before login in!\n\
I create a accout for you, user name is {name}!")
            user_names.append(name)
        else:
            print(f"Hello {name}, thank you for loggin in again!")
else:
    print('We need to find some users!')

print(user_names)