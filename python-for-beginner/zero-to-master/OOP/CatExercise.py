#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

def find_oldest_cat(cats):
    if not cats:
        return None
    oldest = cats[0]
    for cat in cats:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

def main():
    # 1 Instantiate the Cat object with 3 cats
    cindy = Cat('Cindy', 3)
    johny = Cat('Johny', 5)
    chessy = Cat('Chessy', 6)

    # 2 Create a function that finds the oldest cat
    # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
    oldest = find_oldest_cat([cindy, johny, chessy])
    print(f'The oldest cat named {oldest.name} is {oldest.age} years old.')
    
if __name__ == '__main__':
    main()