a = 'apple'[0]
print(a)

b = 'apple'[1]
print(b)

fruit = 'apple'
print(fruit[4])
print(len(fruit))
print('APPLE'.lower())
print('ApplE'.upper())

# String concatinate
print('I' + ' love' + ' python')
print('-' * 10)

# Repeating String
print('-' * 10)
print('happy ' * 10)
print("happy " * 3)
print('-' * 10)

# str() function
print('I love Python ' + str(3) + '.')
print('-' * 10)

# Formatting String
print('I {} Python'.format('love'))
print('{} {} {}'.format('I', 'love', 'Python.'))
print('I {0} {1}. {1} {0} me.'.format('love', 'Python'))
print('I love Python {}.'.format(3))
print('{0:8} | {1:8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:8}'.format('Apply', 5))
print('{0:8} | {1:8}'.format('Oranges', 10))
print('-' * 10)
# Formatting String with alignment
# < ^ > Left Center Right
print('{0:^8} | {1:^10}'.format('Fruit', 'Quantity'))
print('{0:<8} | {1:>10}'.format('Apple', 5))
print('{0:<8} | {1:>10}'.format('Oranges', 10))
print('-' * 10)

# Formatting String with Data Types
# :f as Float, :.Nf as N number of float
print('{:.0f}'.format(2.1111))
print('{0:.0f}'.format(2.1111))
print('{1:.2f}'.format(0, 2))
print('{:.2f}'.format(2.3333))
print('{0:8} | {1:<8}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:<8.2f}'.format('Apple', 5))
print('{0:8} | {1:<8.2f}'.format('Oranges', 10.22222))
print('-' * 10)

# Getting user input
fruit = input('Enter a name of a fruit: ')
print('{} is a lovely fruit'.format(fruit))

# Conclusion
# Built-in functions:
#    print(): Display values
#    len(): Return the length of str
#    str(): Return the str of an object
#    input(): Read a str
# String method: Methods are functions that operate on an object
#    .upper()
#    .lower()
#    .format()
