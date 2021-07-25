def main():
    for i,char in enumerate('Helloooo'):
        print(i, char)

    actions = ['eat', 'sleep', 'repeat']
    for item in enumerate(actions):
        print(item)
    
    for i, item in enumerate(actions):
        print(i, item)
    
    print(list(enumerate(actions)))

    name = 'John'
    print(f'Hello {name}')

if __name__ == '__main__':
    main()