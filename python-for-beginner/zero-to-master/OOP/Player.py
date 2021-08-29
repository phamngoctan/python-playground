# OOP
class PlayerCharacter:
    """
    underscore for private - don't try to change its value
    _name

    double underscore - dunder method - don't modify it
    __init__
    """
    # class object attributes, they are static
    membership = True

    def __init__(self, name='anonymous', age = 0) -> None:
        if PlayerCharacter.membership:
            self._name = name # attributes
            self._age = age
    
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