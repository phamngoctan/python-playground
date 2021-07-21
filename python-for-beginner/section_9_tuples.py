"""
A tuple is an immutable list.
Typles are ordered.
Values accessed by index.
Iteration, looping, concatenation.
Use when data should not change.

tuple_name = (item_1, item_2, item_N)
tuple_name = (item_1,)
"""

days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
monday = days_of_the_week[0]
print(monday)
print()

for day in days_of_the_week:
    print(day)

print('-' * 10)

# Modifying the item inside the tuple will result in an exception

# Convert to list
weekend_tuple = ('Saturday', 'Sunday')
weekend_list = list(weekend_tuple)
print('weekend_tuple is {}'.format(type(weekend_tuple)))
print('weekend_tuple is {}'.format(type(weekend_list)))
print('-' * 10)

# Convert to tuple from a list
animals_list = ['man', 'bear', 'pig']
animals_tuple = tuple(animals_list)
print('animals_lists is {}.'.format(type(animals_list)))
print('animals_tuple is {}.'.format(type(animals_tuple)))
print('-' * 10)

# Looping through a tuple
weekend_days = ('Saturday', 'Sunday')
for day in weekend_days:
    print(day)
print('-' * 10)

# Assign tuple with tuple, with list
(sat, sun) = weekend_days
assert sat == 'Saturday'
assert sun == 'Sunday'
contact_info = ['555-243', 'jason@example.com']
(phone, email) = contact_info
assert phone == '555-243'
assert email == 'jason@example.com'

# Coding practice
def high_and_low(numbers):
    """Determine the highest and lowest number"""
    return (max(numbers), min(numbers))

lottery_numbers = [14, 19, 80, 23, 8, 4]
(highest, lowest) = high_and_low(lottery_numbers)
print('The highest number is: {}'.format(highest))
print('The lowest number is: {}'.format(lowest))
print('-' * 10)

contacts = [('Jason', '555-1433'), ('Carl', '555-0987')]
for (name, phone) in contacts:
    print('{}\'s phone number is {}.'.format(name, phone))
print('-' * 10)

my_wrong_tuple = (1)
assert type(my_wrong_tuple) is not tuple
print(type(my_wrong_tuple))
my_tuple = (1,)
assert type(my_tuple) is tuple
assert isinstance(my_tuple, tuple)
print('-' * 10)

# Exercise
airports = [
    ('O’Hare International Airport', 'ORD'),
    ('Los Angeles International Airport', 'LAX'),
    ('Dallas/Fort Worth International Airport', 'DFW'),
    ('Denver International Airport', 'DEN')
]
for (name, code) in airports:
    print('The code for {} is {}.'.format(name, code))
