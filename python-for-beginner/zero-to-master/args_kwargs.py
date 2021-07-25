
def main():
    # *args **kwargs
    # Rule for order of param: params, *args, default parameters, **kwargs
    total = super_func(1,2,3,4,5, num1=5, num2=10)
    print(total)

def super_func(*args, **kwargs):
    """
    Take any arguments, take any keyword arguments, any number of arguments as we want
    Return sum of all arguments and keyword arguments
    """
    print(args) # --> tuple
    assert args == (1,2,3,4,5)

    print(kwargs) # --> dictionary
    assert kwargs == {
        'num1': 5,
        'num2': 10
    }
    return sum(args) + sum(kwargs.values())

if __name__ == '__main__':
    main()
