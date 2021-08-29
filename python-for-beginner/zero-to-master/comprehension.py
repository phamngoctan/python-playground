# list, set, dictionary comprehension
"""
There is a quick way to create list, set or dictionary 
instead of looping

my_list = [param * 2 for param in iterable if condition (True|False)]

# idea: hey, declare variable named param, for each param as
# an item in the iterable, add it to the list

my_dict = {key:value**2 for key,value in iterable}

Best practice: because the code is shorter, we need to create
a descriptive method name so other dev can be easily to catch up
"""

def print_line_separator():
    print('-' * 10)

def create_list(input):
    my_list = []
    for char in input:
        my_list.append(char)
    return my_list

def create_list_comprehension(input):
    return [param for param in input]

def create_list_in_range(input):
    return [num for num in range(0,50)]

def create_list_with_multiply_by_two_each_item(input):
    return [num *2 for num in range(0, input)]

def create_list_keep_even_number(input):
    return [num ** 2 for num in range(0, input) if num % 2 == 0]

# set playground
def create_set_in_range(input):
    return {num for num in range(0,50)}

def create_dict_from_dict():
    simple_dict = {
        'a': 1,
        'b': 2
    }
    my_dict = {k:v**2 for k,v in simple_dict.items() if v%2 == 0}
    return my_dict

def create_dict_from_list():
    my_dict = {num:num*2 for num in [1,2,3]}
    return my_dict

def main():
    print(create_list('hello'))
    print(create_list_comprehension('hello'))
    print(create_list_in_range(50))

    my_list3 = list(map(lambda i: i * 2, create_list_in_range(50)))
    my_list4 = create_list_with_multiply_by_two_each_item(50)
    print(my_list3)
    assert my_list3 == my_list4
    print_line_separator()
    
    print(create_list_keep_even_number(100))

    # set playground
    print(create_set_in_range(50))

    # dictionary playground
    print(create_dict_from_dict())
    print(create_dict_from_list())

if __name__ == '__main__':
    main()
    