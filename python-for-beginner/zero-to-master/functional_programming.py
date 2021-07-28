# map, filter, zip, and reduce
"""
Use map when we have something iterable & we want to change it
without touching the origin one

Use filter

Use zip when we have two interables, mainly for combine 
into the tuple the data from database which located 
in the diff tables (no sql) but it is in the same order

Use reduce
"""

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 == 0

def accumulator(accumulate, item):
    """
    the accumulate is the initial value
    the item is the item in the origin iterable object
    """
    print(accumulate, item)
    return accumulate + item

def print_line_separator():
    print('-' * 10)

def exec_map_playground(my_list):
    print(list(map(multiply_by2, my_list)))
    print(my_list)
    print_line_separator()

def exec_filter_playground(my_list):
    print(list(filter(only_odd, my_list)))
    print(my_list)
    print_line_separator()

def exec_zip_playground(my_list):
    your_list = [10,20,30]
    their_list = [5,4,3]
    print(list(zip(my_list, your_list, their_list)))
    print(my_list)
    print('-' * 10)

def exec_reduce_playground(my_list):
    from functools import reduce
    # functools is the tool box that includes functions
    print(reduce(accumulator, my_list))
    try:
        reduce(accumulator, [])
    except Exception as ex:
        print(ex)
    print('-' * 10)

def exec_exercise():
    from functools import reduce
    
    #1 Capitalize all of the pet names and print the list
    my_pets = ['sisi', 'bibi', 'titi', 'carla']
    def upper(item):
        return item.upper()
    print(list(map(upper, my_pets)))
    print(list(map(lambda item: item.upper(), my_pets)))

    #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
    my_strings = ['a', 'b', 'c', 'd', 'e']
    my_numbers = [5,4,3,2,1]
    print(list(zip(my_strings, sorted(my_numbers))))

    #3 Filter the scores that pass over 50%
    scores = [73, 20, 65, 19, 76, 100, 88]
    def filter_pass_score(score):
        return score > 50
    print(list(filter(filter_pass_score, scores)))
    print(list(filter(lambda score: score > 50, scores)))

    #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
    def number_accumulator(accumulator, initial):
        return initial + accumulator
    # my_numbers.extend(scores)
    reduce1 = reduce(number_accumulator, my_numbers + scores, 0)
    print(reduce1)
    print(reduce(lambda accumulator, initial_val: initial_val + accumulator, my_numbers + scores, 0))

def main():
    my_list = [1, 2, 3]
    exec_map_playground(my_list)
    
    exec_filter_playground(my_list)

    exec_zip_playground(my_list)

    exec_reduce_playground(my_list)

    exec_exercise()

if __name__ == '__main__':
    main()
