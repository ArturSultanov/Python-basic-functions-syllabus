favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

friends = []

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
    
    if language == 'python':
        friends.append(name)

for name in favorite_languages.keys():
    if name in friends:
        print(f"Hi {name.title()}, I see\
 your fav language is {favorite_languages[name].title()}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    favorite_languages['erin'] = 'swift'

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())

