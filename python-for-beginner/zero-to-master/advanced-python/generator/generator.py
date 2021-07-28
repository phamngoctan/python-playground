# interable
# iterate
# generators (subset of iterable)

# how to create a generator
# when there is a yield, it is a generator
# it keeps the most recent value in memory
def generator_function(num):
    for i in range(10):
        yield i*2
     
def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

# my_list = make_list(100)
generator = generator_function(10)
next(generator) # 0 * 2 = 0
next(generator) # 1 * 2 = 2
print(next(generator)) # 2 * 2 = 4