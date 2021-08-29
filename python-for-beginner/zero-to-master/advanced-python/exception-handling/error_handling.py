while True:
    try:
        age = int(input('Please enter you age: '))
        10/age
    except ValueError:
        print('Please enter a number')
    except ValueError:
        print('!!!!')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print(f'Your age is {age} years old')
        print('Thank you')
        break

def devision(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError) as ex:
        print(f'ooooops {ex}')

print(devision(1,0))

try:
    raise ValueError('Hey cut it out')
except ValueError as ex:
    print(f'Exception happens: {ex}')