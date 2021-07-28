some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

def find_duplicated(some_list):
    duplicates = []
    for value in some_list:
        if some_list.count(value) > 1:
            if value not in duplicates:
                duplicates.append(value)
    return duplicates

def find_duplicated_comprehension(some_list):
    return list({num for num in some_list if some_list.count(num) > 1})

print(find_duplicated(some_list))
print(find_duplicated_comprehension(some_list))

