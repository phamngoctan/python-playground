# OOP
class PlayerCharacter:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def run(self):
        print('run')
    
def main():
    player1 = PlayerCharacter('Cindy', 22)
    player2 = PlayerCharacter('Tom', 40)
    print(player1)
    print(player2)

if __name__ == '__main__':
    main()