aliens = []
for alien_number in range(30):
    new_alien = {
        'number': alien_number,
        'color': 'green',
        'points': 5,
        'speed': 'slow'
        }
    aliens.append(new_alien)

aliens[1]['color'] = 'yellow'

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")
