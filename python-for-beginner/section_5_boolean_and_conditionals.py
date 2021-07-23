"""
Order of Operations for Booleans
not
and
or
"""
def control_order_by_parenthesis():
    print((True and False) or (not False))

print(True and False or not False)
control_order_by_parenthesis()
print('-' * 10)

# if condition
def hello_ages(age:int):
    if age > 35:
        print('You are old enough to be a Senator or the President.')
    elif age > 30:
        print('You are old enough to be a Senator.')
    else:
        print('You are not old enough to be a Senator or the President.')
    print('Have a nice day!')
hello_ages(45)
hello_ages(32)
hello_ages(20)
print('-' * 10)

# Exercise 1
def suggest_travelling(distance:int):
    if distance >= 300:
        print('I suggest flying to your destination.')
    elif distance >= 3:
        print('I suggest driving to your destination.')
    else:
        print('I suggest walking to your destination.')
def ask_user_distance() -> int:
    distance = input('How far would you like to travel in miles? ')
    return int(distance)
suggest_travelling(ask_user_distance())