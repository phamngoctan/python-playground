# Exercise 1
def exec_exercise1():
    animal = 'cat'
    vegatable = 'broccoli'
    mineral = 'gold'
    print('Here is an animal, a vegatable, and a mineral')
    print('cat')
    print('broccoli')
    print('gold')

# Exercise 2
def exec_exercise2():
    userInput = input('Please type something and press enter: ')
    print('You entered: {}'.format(userInput))

# Exercise 3
def printCat():
    print('{}/'.format(' ' * 11))
    print('{0:^7}   /'.format('/\\_/\\'))
    print('{0:7}'.format('( o.o )'))
    print('{0:^7}'.format('> ^ <'))

def create_top_border(text_length:int):
    print('{} {}'.format(' ' * 11, '_' * text_length))

def create_body(input_text:str):
    print('{}< {} >'.format(' ' * 11, input_text))

def create_bottom_border(text_length):
    print('{} {}'.format(' ' * 11, '-' * text_length))

def exec_exercise3():
    text = input('What would you like the cat to say? ')
    create_top_border(len(text))
    create_body(text)
    create_bottom_border(len(text))
    printCat()

def main():
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

    exec_exercise3()
if __name__ == '__main__':
    main()