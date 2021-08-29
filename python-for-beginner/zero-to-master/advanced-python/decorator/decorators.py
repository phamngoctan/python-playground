"""
by doing this, we let the Python interpretor know that we
want to add some extra features to it

Decorator super charges a function

@decorator 
def hello()
    pass

"""

# Higher Order Function (HOC)
# A function that accepts another function inside
# filter, map, ... are the HO

def core_of_decorators():
    def hello(func):
        print('Helllllloooooooooo')
        func()

    def greet():
        print('Still here!')

    a = hello(greet)
    print(a)

# Decorator Pattern
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func

@my_decorator
def hello():
    print('Helllloooooooo')

@my_decorator
def hello_complex(greeting, emoji=':('):
    print(greeting, emoji)

# @my_decorator
def bye():
    print('see ya later')

def main():
    hello()
    bye()
    print('-' * 10)

    # Under the hood, Python interpreter does:
    bye2 = my_decorator(bye)
    bye2()
    print('-' * 10)
    
    # complex decorator
    hello_complex('hiiii')
    

if __name__ == '__main__':
    main()
