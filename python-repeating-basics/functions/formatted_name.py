def get_formatted_name(first_name, last_name, mid_name=''):
    if mid_name:
        full_name = first_name + ' ' + mid_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

jimi = get_formatted_name('jimi', 'hendrix')
eddie = get_formatted_name('eddie', 'van', 'halen')
print(jimi)
print(eddie)
