def build_person(first_name, last_name, band='', age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    if band:
        person['band'] = band
    return person

musician = build_person('kurt', 'cobain', age=27, band='Nirvana')
print(musician)
