# Lists
"""
# declare the list
list_name = [item_1, item_2, item_n]
list_name = []

# access the list
list_name[index]
"""
animals = ['man', 'bear', 'pig']
print(animals[0])
animals[0] = 'cat'
print(animals[0])
print('-' * 10)

# Accessing List with negative index
humans = ['John', 'Daniel', 'Peter']
print(humans[-1])
print(humans[-2])
print(humans[-3])

# Add item to the List
# The last item is always index with -1
humans.append('Bob')
print(humans[-1])
more_humans = ['Lena', 'Lexy']
humans.extend(more_humans)
print('Last two humans: {} {}'.format(humans[-1], humans[-2]))
"""Insert before the last item in the List"""
humans.insert(len(humans) - 1, 'Grass')
assert humans[-2] == 'Grass', "It should equal Grass value"

# Slices
"""
Slice from index1 (inclusive) to index2 (not inclusive)
list[index1:index2]

index1 = 0 by default
list[:index2]

index2 = len(list) by default
list[index1:]
"""
animals = ['man', 'bear', 'pig', 'cow', 'duck', 'horse']
some_animals = animals[1:4]
assert some_animals == ['bear', 'pig', 'cow']
first_two = animals[0:2]
assert first_two == ['man', 'bear']
first_two_again = animals[:2]
assert first_two_again == ['man', 'bear']
last_two = animals[4:6]
assert last_two == ['duck', 'horse']
last_two_again = animals[-2:]
assert last_two_again == ['duck', 'horse'], 'but it is {}'.format(last_two_again)
print('-' * 10)

# Slicing list part 2
basket = ['a', 'x', 'b', 'd', 'c', 'd', 'e']
basket.sort()
basket.reverse()
reverted_basket = basket[::-1]
print(reverted_basket)
print(basket)
print(list(range(1, 100))) # 1 -> 99

# List unpacking
try:
    a,b,c = ['1', '2', '3', '4', '4', '6']
except Exception as ex:
    print(ex)

a,b,c, *other, d = ['1', '2', '3', '4', '4', '6', '9']
assert a == '1' and b == '2' and c == '3'
assert other == ['4', '4', '6']
assert d == '9'
print('-' * 10)

# String Slices
part_of_a_horse = 'horse'[1:3]
assert part_of_a_horse == 'or'
print('-' * 10)

# String join
sentence = '!'
new_sentence = sentence.join(['My', 'name', 'is', 'John'])
print(new_sentence)
assert new_sentence == 'My!name!is!John'

print('-' * 10)

# Finding an item in a list
animals = ['man', 'bear', 'pig']
bear_index = animals.index('bear')
assert bear_index == 1

# Exception Handling
animals = ['man', 'bear', 'pig']
try:
    cat_index = animals.index('cat')
except:
    cat_index = 'no cats found.'
print(cat_index)
print('-' * 10)

# For Loop
animals = ['man', 'bear', 'pig']
for animal in animals:
    print(animal.upper())
print('-' * 10)

# While Loop
animals = ['man', 'bear', 'pig']
index = 0
while index < len(animals):
    print(animals[index])
    index += 1
print('-' * 10)

# Sorting
animals = ['man', 'bear', 'pig']
sorted_animals = sorted(animals) # not touch the origin animals
print('Animals list: {:>30}'.format(str(sorted_animals)))
assert animals == ['man', 'bear', 'pig']

animals.sort() # sort in the input list
print('Animals list: {:>30}'.format(str(animals)))
assert animals == ['bear', 'man', 'pig']
print('-' * 10)

# len function
animals = ['man', 'bear']
assert len(animals) == 2

# Ranges
for number in range(3): # stop only, start: assume 0
    print(number)
print('-' * 10)
for number in range(1, 3): # start, stop
    print(number)
print('-' * 10)
for number in range(1, 10, 2): # 2 is the jumped steps
    print(number)
print('-' * 10)

# Exercises
def get_tasks_from_keyboards():
    tasks = []
    while True:
        text = input('Enter a task for your to­do list. Press <enter> when done:')
        if len(text) == 0:
            return tasks
        else:
            tasks.append(text)

def show_tasks(tasks):
    print('Your To-Do List:')
    print('-' * 20)
    for task in tasks:
        print(task)
 
def exec_exercise_1():
    tasks = get_tasks_from_keyboards()
    show_tasks(tasks)

exec_exercise_1()

