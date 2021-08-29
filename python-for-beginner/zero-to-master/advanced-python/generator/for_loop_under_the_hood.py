"""
How the for loop really works
"""
def special_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator) # memory address of iterator
            print(next(iterator) * 2) # get value of the iterator * 2 and change to the next iterator
        except StopIteration:
            break
special_for_loop([1,2,3])

