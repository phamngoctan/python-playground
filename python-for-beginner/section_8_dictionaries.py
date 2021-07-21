# Hold key-value pairs called items.
# Like HashMap in Java
# dictionary_name = {key_1: val_1, key_n: value_n}
# dictionary_name = {}
# dictionary_name[key]

contacts = {'Jason': '555-1234', 'Carl': '555-0987'}
contacts['Jason'] = '555-1233'
jason_phone = contacts['Jason']
carl_phone = contacts['Carl']
print('Dial {} to call Jason.'.format(jason_phone))
print('Dial {} to call Carl.'.format(carl_phone))
print('Phone book length: {}'.format(len(contacts)))

# Delete item from the dictionary
contacts = {'John': 111222}
del contacts['John']
assert len(contacts) == 0

# Multiple object types in value of the dictionary
contacts = {
    'Jason': ['555-123', 123456],
    'Carl': '54321'
}
for number in contacts['Jason']:
    print('Phone: {}'.format(number))
print('-' * 10)

# Check if a key exists
contacts = {
    'Jason': ['555-123', 123456],
    'Carl': '54321'
}
if 'Jason' in contacts.keys():
    print('Jason\'s phone number is: {}'.format(contacts['Jason']))
print('-' * 10)

# Check if a value exists
contacts = {
    'Jason': ['555-123', 123456],
    'Carl': '54321'
}
if '54321' in contacts.values():
    print('The phone {} is in the contacts'.format('555-123'))
assert ['555-123', 123456] in contacts.values()
print('-' * 10)

# Loops
contacts = {
    'Jason': ['555-123', 123456],
    'Carl': '54321'
}
for key in contacts:
    print('{} has phone {}'.format(key, contacts[key]))

for name, phone in contacts.items():
    print('{} has phone {}'.format(name, str(phone)))
print('-' * 10)

# Exercise
person_feelings = {
    'Jeff': ' Is afraid of clowns.',
    'David': 'Plays the piano.',
    'Jason': 'Can fly an airplane.'
}
def show_person_feeling():
    for person, feeling in person_feelings.items():
        print('{}: {}'.format(person, feeling))
show_person_feeling()
print('')
person_feelings['Jill'] = 'Can hula dance.'
show_person_feeling()
print('-' * 10)
# The insertion order of dictionary from Python version >= 3.6 is guaranteed
