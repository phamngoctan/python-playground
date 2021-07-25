# OOP
class PlayerCharacter:
    # class object attributes, they are static
    membership = True

    def __init__(self, name='anonymous', age = 0) -> None:
        if PlayerCharacter.membership:
            self.name = name # attributes
            self.age = age
    
    def shout(self):
        print(f'My name is {self.name}')
    
def main():
    player1 = PlayerCharacter('Cindy', 22)
    player2 = PlayerCharacter('Tom', 40)
    player1.shout()
    player2.shout()
    # player2.attack = 10

    # help(PlayerCharacter)

if __name__ == '__main__':
    main()