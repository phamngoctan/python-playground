# follow the idea to implement custom range

class MyGenerator():
    # class object attribute
    current = 0

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGenerator.current < self.last:
            num = MyGenerator.current
            MyGenerator.current += 1
            return num
        raise StopIteration

gen = MyGenerator(0, 100)
for i in gen:
    print(i)