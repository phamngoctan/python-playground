# Function
def say_hi(name):
    print('Hi {}!'.format(name))
say_hi('Tan Pham')
print('-' * 10)

# Function with optional parameter 
def say_hello(first, last='Doe'):
    """Say hello"""
    print('Hello {} {}!'.format(first, last))
say_hello('Jane')
say_hello('Tan', 'Pham')
say_hello(last = 'Pham', first='Tan')
print('-' * 10)

# Documents of a method - docstring
"""
Use above method
help(say_hello)
--> it prints out
say_hello(first, last='Doe'):
    Say hello
"""

# Return value
def is_odd(number):
    """Determine if a number is odd."""
    if number % 2 == 0:
        return False
    else:
        return True
print(is_odd(7))
print('-' * 10)

# Exercise
"""
Newton
England
"""
story = "Isaac {} was born in Lincolnshire, {} in 1643, where he grew up on a farm. When he was a boy, he made lots of brilliant inventions like a windmill to grind corn, a water clock and a sundial. However, Isaac didn’t get brilliant marks at school."

def show_story():
    """Show the story to user"""
    print(story.format('___', '___'))
def get_user_input():
    """Get the input from user"""
    user_input1 = input('Enter the first blank: ')
    user_input2 = input('Enter the second blank: ')
    return [user_input1, user_input2]
def display_full_story(input1, input2):
    print('Here is the full story you created. Enjoy!')
    print(story.format(input1, input2))

show_story()
input_from_user = get_user_input()
display_full_story(input_from_user[0], input_from_user[1])
print('-' * 10)